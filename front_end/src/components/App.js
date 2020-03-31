import React, {Component} from 'react';
import {Route, Switch} from 'react-router-dom';

import Dashboard from './Dashboard/Dashboard';
import Login from '../components/Login'
import PrivateRoute from '../common/PrivateRoute'

class App extends Component {
  render() {
    return (
      <Switch>
        <PrivateRoute exact path="/" component={Dashboard} />
        <Route exact path="/login" component={Login} />
      </Switch>
    );
  }
}

export default App;
