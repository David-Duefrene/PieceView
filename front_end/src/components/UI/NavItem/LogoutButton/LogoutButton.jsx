import React from 'react';
import PropTypes from 'prop-types';

import CSS from './LogoutButton.module.css';

/**
 * Renders an individual navigation item for the navigation bar.
 * @param {func} props.logoutReducer - The function to logout the user.
 */
const logoutButton = (props) => {
    const { logoutReducer, children } = props;
    return (
        <li className={CSS.LogoutButton}>
            <a
                to='/'
                onClick={logoutReducer}
                onKeyDown={logoutReducer}
                exact='True'
                role='button'
                tabIndex={0}
            >
                {children}
            </a>
        </li>
    );
};

logoutButton.propTypes = {
    logoutReducer: PropTypes.func.isRequired,
    children: PropTypes.string,
};

logoutButton.defaultProps = { children: 'logout' };

export default logoutButton;
