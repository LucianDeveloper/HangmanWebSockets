import ky from 'ky';
import {notification} from 'antd';
import {get} from './storage';
import historyRef from './history';

const api = (url, {headers, ...options} = {}) => {
	console.log('Cookie:', document.cookie)
	return ky(
		`http://127.0.0.1:8000${url}`,
		{
			timeout: 2 * 60 * 1000,
			headers: {
				...headers
			},
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
	).json();
}

export default api;
