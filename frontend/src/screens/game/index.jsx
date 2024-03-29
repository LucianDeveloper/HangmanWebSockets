import React from 'react';
import {notification, Spin} from 'antd';
import {Switch, Route, Redirect, useRouteMatch} from 'react-router-dom';
import api from '../../utils/api';
import GameComponent from '../../components/game'
import Layout from '../../components/layout';


const Game = () => {
	const {path} = useRouteMatch();
	const [user, setUser] = React.useState(null);
	React.useEffect(
		() => {
			const load = async () => {
				const {email} = await api('/users/me');
				setUser(email);
			};

			load().catch((err) => {
				notification.error({
					message: 'Произошла ошибка при загрузке данных о пользователе',
					description: err.message
				})
			});
		},
		[]
	);

	if (!user)
		return (
			<div className="vh-100 vw-100 d-flex align-items-center justify-content-center">
				<Spin size="large" tip="Загрузка данных о пользователе" />
			</div>
		);

	return (
		<Layout email={user}>
			<Switch>
				<Route path={`${path}/play`}>
					<GameComponent />
				</Route>
				<Route exact path={path}>
					<Redirect to={`${path}/play`} />
				</Route>
			</Switch>
		</Layout>
	);
};

export default Game;
