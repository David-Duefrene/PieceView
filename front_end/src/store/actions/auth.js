import authAxios from '../../axios-auth';
import axios from '../../axios';
import { returnErrors } from './messages';
import * as actions from './actionTypes';

/**
 * Logs a user in and get the authentication token from the server.
 * @param {string} username The user's username.
 * @param {string} password The user's password.
 */
export const login = (username, password) => (dispatch) => {
    // Request Body
    const body = JSON.stringify({ username, password });

    axios.post('account/api/auth/login', body)
        .then((result) => {
            dispatch({ type: actions.LOGIN_SUCCESS, payload: result.data });
        }).catch((error) => {
            dispatch(returnErrors(error.response.data, error.response.status));
        });
};

export const updateProfile = (profile) => (dispatch) => {
    authAxios.patch('/account/api/account/edit', profile).then((result) => {
        dispatch({ type: actions.UPDATE_PROFILE, payload: result.data });
    }).catch((error) => new Error(error));
};

/**
 * Registers the user with the server.
 * @param {string} username The user's username.
 * @param {string} password The user's password.
 * @param {string} email The user's email.
 */
export const register = (newUser) => (dispatch) => {

    axios.post('account/api/account', newUser).then((result) => {
        dispatch({
            type: actions.LOGIN_SUCCESS,
            payload: result.data,
        });
    }).catch((error) => {
        dispatch(returnErrors(error.response.data, error.response.status));
    });
};

/**
 * Logs the user out and invalidates the authentication key with the server.
 */
export const logout = () => (dispatch) => {
    dispatch({ type: actions.LOGOUT_SUCCESS });
};
