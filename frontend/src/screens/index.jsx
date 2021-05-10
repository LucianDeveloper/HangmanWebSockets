import React from 'react';
import {BrowserRouter as Router, Switch, Route, Redirect} from 'react-router-dom';
import Login from './Login';
import Game from './game';
import HistoryThief from '../components/utils/HistoryThief';

const Screens = () => (
	<Router>
		<HistoryThief />
		<Switch>
			<Route path="/login">
				<Login />
			</Route>
			<Route path="/game">
				<Game />
			</Route>
			<Route exact path="/">
				<Redirect to="/game" />
			</Route>
		</Switch>
	</Router>
);

export default Screens;
