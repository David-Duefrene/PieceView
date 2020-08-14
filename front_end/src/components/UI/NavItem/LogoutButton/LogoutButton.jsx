import React from 'react';
import PropTypes from 'prop-types';

import CSS from './LogoutButton.module.css';

/**
 * Renders an individual navigation item for the navigation bar.
 * @param {func} logoutReducer - The function to logout the user.
 */
const LogoutButton = (props) => {
    const { logoutReducer, children } = props;

    return (
        <li className={CSS.LogoutButton}>
            <a
                to='/'
                onClick={() => {
                    localStorage.removeItem('token');
                    localStorage.removeItem('user');
                }}
                exact='True'
                role='button'
                tabIndex={0}
            >
                {children}
            </a>
        </li>
    );
};

LogoutButton.propTypes = {
    logoutReducer: PropTypes.func.isRequired,
    children: PropTypes.string,
};

LogoutButton.defaultProps = { children: 'logout' };

export default LogoutButton;
