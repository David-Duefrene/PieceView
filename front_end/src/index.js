import ReactDOM from 'react-dom';
import React, {Component} from 'react';
import {Provider} from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';

import App from './App'
import store from './store'


class ErrorBoundary extends Component {
    state = { hasError: false };

    static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    console.log(error);
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


class Index extends Component {
    render() {
        return (
            <ErrorBoundary>
            <Provider store={store}>
                <Router>
                <App />
                </Router>
            </Provider>
            </ErrorBoundary>
        );
    }
}

ReactDOM.render(<Index />, document.getElementById('root'));
