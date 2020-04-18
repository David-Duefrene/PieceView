import React, {Component} from 'react';
import {Route, Switch} from 'react-router-dom';

import Dashboard from './containers/Dashboard/Dashboard';
import Login from './containers/Auth/Login/Login';
import PrivateRoute from './common/PrivateRoute';
import NavBar from './containers/NavBar/NavBar';
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
