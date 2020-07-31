import React from 'react';
import { Route, Switch } from 'react-router-dom';

import Posts from './containers/Posts/Posts';
import Dashboard from './containers/Dashboard/Dashboard';
import Login from './containers/Auth/Login/Login';
import Register from './containers/Auth/Register/Register';
import PrivateRoute from './common/PrivateRoute';
import NavBar from './containers/NavBar/NavBar';
import CSS from './App.module.css';

const App = () => (
    <div className={CSS.App}>
        <NavBar />
        <Switch>
            <Route exact path='/' component={Posts} />
            <PrivateRoute exact path='/dashboard' component={Dashboard} />
            <Route exact path='/login' component={Login} />
            <Route exact path='/register' component={Register} />
        </Switch>
    </div>
);

export default App;
