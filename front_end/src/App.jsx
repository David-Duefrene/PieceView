import React from 'react';
import { Route, Switch } from 'react-router-dom';

import Posts from './components/Posts/Posts';
import CreatePost from './components/Posts/CreatePost/CreatePost';
import Post from './components/Posts/Post/Post';
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
            <Route path='/login' component={Login} />
            <Route path='/register' component={Register} />
            <Route path='/post/:pk' component={Post} />
            <PrivateRoute path='/create-post' component={CreatePost} />
            <PrivateRoute path='/dashboard' component={Dashboard} />
        </Switch>
    </div>
);

export default App;
