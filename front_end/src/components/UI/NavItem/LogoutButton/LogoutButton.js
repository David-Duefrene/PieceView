import React from "react";
import PropTypes from 'prop-types';

import CSS from './LogoutButton.module.css'


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
