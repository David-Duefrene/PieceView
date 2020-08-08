/* eslint-disable react/prop-types */
import React, { Component } from 'react';

export class ErrorBoundary extends Component {
    state = { hasError: false, error: null, errorInfo: null };

    // Update state so the next render will show the fallback UI.
    static getDerivedStateFromError(error) { return { hasError: true, error }; }

    componentDidCatch(error, errorInfo) {
        this.setState({
            hasError: true, error, errorInfo,
        });
    }

    render() {
        const { hasError, error, errorInfo } = this.state;
        const { children } = this.props;
        if (hasError) {
            // You can render any custom fallback UI
            return (
                <div>
                    <h1>Something went wrong.</h1>
                    <p>{error && error.toString()}</p>
                    <br />
                    <p>{errorInfo.componentStack}</p>
                </div>
            );
        }
        return children;
    }
}

export default ErrorBoundary;
