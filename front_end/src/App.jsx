import React from 'react';
import { Route, Switch } from 'react-router-dom';

import CreatePost from './components/Posts/CreatePost/CreatePost';
import Post from './components/Posts/Post/Post';
import Dashboard from './containers/Dashboard/Dashboard';
import Login from './containers/Auth/Login/Login';
import Register from './containers/Auth/Register/Register';
import PrivateRoute from './common/PrivateRoute';
import NavBar from './containers/NavBar/NavBar';
import UserProfile from './components/UserProfile/UserProfile';
import HomePage from './components/HomePage/HomePage';
import CSS from './App.module.css';

const App = () => (
    <div className={CSS.App}>
        <NavBar />
        <Switch>
            <Route exact path='/' component={HomePage} />
            <Route path='/login' component={Login} />
            <Route path='/register' component={Register} />
            <Route path='/post/:pk' component={Post} />
            <Route path='/user/:pk' component={UserProfile} />
            <PrivateRoute path='/create-post' component={CreatePost} />
            <PrivateRoute path='/dashboard' component={Dashboard} />
        </Switch>
    </div>
);

export default App;
