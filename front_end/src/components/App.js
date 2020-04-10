import React, {Component} from 'react';
import {Route, Switch} from 'react-router-dom';

import Dashboard from './Dashboard/Dashboard';
import Login from '../components/Login';
import PrivateRoute from '../common/PrivateRoute';
import NavBar from './Navigation/NavBar/NavBar';
import CSS from './App.module.css';

class App extends Component {
  render() {
    return (
      <div className={CSS.App}>
        <NavBar />
        <Switch>
          <PrivateRoute exact path="/" component={Dashboard} />
          <Route exact path="/login" component={Login} />
        </Switch>
      </div>
    );
  }
}

export default App;
