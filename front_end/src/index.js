import ReactDOM from 'react-dom';
import React from 'react';
import { Provider } from 'react-redux';
import {
  HashRouter as Router,
  Route, Switch
} from 'react-router-dom';

import App from './components/App'
import Login from './components/Login'
import PrivateRoute from './common/PrivateRoute'
import store from './store'


class Index extends React.Component {
  render(){
    return (
      <Provider store={store}>
        <Router>
        <React.Fragment>
          <div className="container">
            <Switch>
              <PrivateRoute exact path="/" component={App} />
              <Route exact path="/login" component={Login} />
            </Switch>
          </div>
        </React.Fragment>
        </Router>
      </Provider>
    )
  }
}

ReactDOM.render(<Index />, document.getElementById('root'));
