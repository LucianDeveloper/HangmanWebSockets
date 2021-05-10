import ky from 'ky';
import {get} from './storage';
import {notification} from 'antd';
import historyRef from './history';


const rawApi = (url, {headers, ...options} = {}) =>
	ky(
		`http://localhost:8000${url}`,
		{
			timeout: 2 * 60 * 1000,
			headers: {
				...headers
			},
			credentials: 'include',
			hooks: {
				afterResponse: [
					(request, options, response) => {
						if (response.status === 401) {
							notification.error({
								message: 'Сессия истекла, выполните вход повторно',
								description: response.statusText
							});
							historyRef.history.push('/login');
						} else if (response.status >= 400) {
							notification.error({
								message: 'Ошибка выполнения запроса',
								description: response.statusText
							});
						} else if (!response.ok) {
							notification.error({
								message: 'Ошибка выполнения запроса',
								description: 'Нераспознанная ошибка'
							});
						}
					}
				]
			},
			...options
		}
	);


export default rawApi;
