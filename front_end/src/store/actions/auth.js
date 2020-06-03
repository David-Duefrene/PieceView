import axios from 'axios';

import { returnErrors } from './messages';
import * as actions from './actionTypes';


/**
 * Loads a user object from the server.
 */
export const loadUser = () => (dispatch, state) => {
    dispatch({ type: actions.USER_LOADING });

    axios.get(
        'http://localhost:8000/account/api/auth/user',
        tokenConfig(state)).then(result => {
            dispatch({
                type: actions.USER_LOADED,
                payload: result.data,
            });
        }).catch(error => {
            dispatch(returnErrors(error.response.data, error.response.status));
            dispatch({
                type: actions.AUTH_ERROR
            });
        });
};


/**
 * Logs a user in and get the authentication token from the server.
 * @param {string} username The user's username.
 * @param {string} password The user's password.
 */
export const login = (username, password) => dispatch => {
    // Headers
        const config = {
        headers: { 'Content-Type': 'application/json' }
    };

    // Request Body
    const body = JSON.stringify({ username, password });

    axios.post('http://127.0.0.1:8000/account/api/auth/login', body, config)
    .then(result => {
        dispatch({
            type: actions.LOGIN_SUCCESS,
            payload: result.data,
        });
    }).catch(error => {
        dispatch(returnErrors(error.response.data, error.response.status));
        dispatch({ type: actions.LOGIN_FAIL });
    });
};


/**
 * Registers the user with the server.
 * @param {string} username The user's username.
 * @param {string} password The user's password.
 * @param {string} email The user's email.
 */
export const register = newUser => dispatch => {
    // Headers
        const config = {
        headers: { 'Content-Type': 'application/json' }
    };

    axios.post(
        'http://localhost:8000/account/api/auth/register',
        newUser,
        config
    ).then(result => {
        dispatch({
            type: actions.LOGIN_SUCCESS,
            payload: result.data,
        });
    }).catch(error =>  {
        console.log(error.response);
    })
};


/**
 * Logs the user out and invalidates the authentication key with the server.
 */
export const logout = () => ( dispatch, getState ) => {
    fetch('http://localhost:8000/account/api/auth/logout',
        null,
        tokenConfig(getState)).then(raw => {
            return raw.json();
        }).then(() => {
            dispatch({ type: actions.LOGOUT_SUCCESS });
        },
    (error) => {
        console.log(`Error in actions.auth.js in logout().\nError:  ${error}`);
    });
};


/**
 * Sets the config with the user's token.
 * @param {object} getState Current state.
 */
export const tokenConfig = getState => {
    // Get token from state
    const token = getState().auth.token;

    // Headers
    const config = {
        headers: { 'Content-Type': 'application/json' },
    };

    // If token, add to headers config
    if (token) { config.headers['Authorization'] = `Token ${token}` };

    return config;
};
