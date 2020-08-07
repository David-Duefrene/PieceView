import React from 'react';
import { Route, Switch } from 'react-router-dom';

import Posts from './containers/Posts/Posts';
import Post from './components/Post/Post';
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
            <PrivateRoute path='/dashboard' component={Dashboard} />
            <Route path='/login' component={Login} />
            <Route path='/register' component={Register} />
            <Route path='/post/:pk' component={Post} />
        </Switch>
    </div>
);

export default App;
