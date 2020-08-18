import React from 'react';
import PropTypes from 'prop-types';
import { useDispatch } from 'react-redux';

import * as actions from '../../../../store/actions/actionTypes';
import CSS from './LogoutButton.module.css';

/**
 * Renders an individual navigation item for the navigation bar.
 */
const LogoutButton = (props) => {
    const { children } = props;
    const dispatch = useDispatch();

    return (
        <li className={CSS.LogoutButton}>
            <a
                to='/'
                onClick={() => dispatch({ type: actions.LOGOUT_SUCCESS })}
                onKeyDown={() => dispatch({ type: actions.LOGOUT_SUCCESS })}
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
    children: PropTypes.string,
};

LogoutButton.defaultProps = { children: 'logout' };

export default LogoutButton;
