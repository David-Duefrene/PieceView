import React from 'react';
import PropTypes from 'prop-types';

import CSS from './LogoutButton.module.css';


/**
 * Renders an individual navigation item for the navigation bar.
 * @param {func} props.logoutReducer - The function to logout the user.
 */
const logoutButton = props => {
    return (
        <li className={CSS.LogoutButton} >
            <a
                to='/'
                onClick={props.logoutReducer}
                exact='True' >
                {props.children}
            </a>
        </li>
    );
}

logoutButton.propTypes = { logoutReducer: PropTypes.func };

export default logoutButton;
