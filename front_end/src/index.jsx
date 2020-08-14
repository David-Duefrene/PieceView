import ReactDOM from 'react-dom';
import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';

import App from './App';
import store from './store';
import ErrorBoundary from './common/ErrorBoundary';

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
