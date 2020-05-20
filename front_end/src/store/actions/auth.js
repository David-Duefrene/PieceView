import axios from 'axios';

import { returnErrors } from './messages';
import * as actions from './actionTypes';

export const loadUser = () => (dispatch, getState) => {
    dispatch({ type: actions.USER_LOADING });

    axios.get(
        "http://localhost:8000/account/api/auth/user",
        tokenConfig(getState)).then(result => {
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

export const login = (username, password) => dispatch => {
    // Headers
        const config = {
        headers: { "Content-Type": "application/json" }
    };

    // Request Body
    const body = JSON.stringify({ username, password });

    axios.post("http://localhost:8000/account/api/auth/login", body, config)
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

export const register = ({ username, password, email }) => dispatch => {
    // Headers
        const config = {
        headers: { "Content-Type": "application/json" }
    };

    // Request Body
    const body = JSON.stringify({ username, email, password });

    const payload = {
        method: 'POST',
        mode: 'same-origin',
        body: body,
        headers: config,
    };

    fetch('http://localhost:8000/api/auth/register', payload).then(raw => {
        return raw.json();
    }).then(result => {
        console.log(`Result: ${result}`);
    },
    (error) =>  {
        console.log(`Error in actions.auth.js line 86.\nError ${error}`)
    })
};

export const logout = () => ( dispatch, getState ) => {
    fetch('http://localhost:8000/account/api/auth/logout',
        null,
        tokenConfig(getState)).then(raw => {
        return raw.json();
    }).then(() => {
        dispatch({ type: actions.LOGOUT_SUCCESS });
    },
    ( error ) => {
        console.log(`Error in actions.auth.js in logout().\nError:  ${error}`);
    });
};

// Setup config with token
export const tokenConfig = getState => {
    // Get token from state
    const token = getState().auth.token;

    // Headers
    const config = {
        headers: { "Content-Type": "application/json" },
    };

    // If token, add to headers config
    if (token) { config.headers["Authorization"] = `Token ${token}` };

    return config;
};
