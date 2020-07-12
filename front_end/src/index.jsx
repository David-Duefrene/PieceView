/* eslint-disable react/prop-types */
/* eslint-disable max-classes-per-file */
import ReactDOM from 'react-dom';
import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';

import App from './App';
import store from './store';

class ErrorBoundary extends Component {
    state = { hasError: false, error: null };

    // Update state so the next render will show the fallback UI.
    static getDerivedStateFromError(error) { return { hasError: true, error }; }

    render() {
        const { hasError, error } = this.state;
        const { children } = this.props;
        if (hasError) {
            // You can render any custom fallback UI
            return (
                <div>
                    <h1>Something went wrong.</h1>
                    <p>{JSON.stringify(error)}</p>
                </div>
            );
        }
        return children;
    }
}

const Index = () => (
    <ErrorBoundary>
        <Provider store={store}>
            <Router>
                <App />
            </Router>
        </Provider>
    </ErrorBoundary>
);

ReactDOM.render(<Index />, document.getElementById('root'));
