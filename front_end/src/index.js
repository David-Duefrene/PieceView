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


class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return (
        <div>
          <h1>Something went wrong.</h1>
          <p>{JSON.stringify(this.state)}</p>
        </div>
      );
    }
    return this.props.children; 
  }
}


class Index extends React.Component {
  render(){
    return (
      <ErrorBoundary>
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
      </ErrorBoundary>
    )
  }
}

ReactDOM.render(<Index />, document.getElementById('root'));
