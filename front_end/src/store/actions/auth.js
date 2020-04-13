import axios from "axios";

import { returnErrors } from "./messages";
import {
  USER_LOADING, USER_LOADED, AUTH_ERROR, LOGIN_SUCCESS, LOGIN_FAIL,
  LOGOUT_SUCCESS,
} from "./actionTypes"

export const loadUser = () => (dispatch, getState) => {
  dispatch({ type: USER_LOADING });

  axios.get("http://localhost:8000/account/api/auth/user", tokenConfig(getState)).then(res => {
    dispatch({
      type: USER_LOADED,
      payload: res.data
    });
  }).catch(err => {
    dispatch(returnErrors(err.response.data, err.response.status));
    dispatch({
      type: AUTH_ERROR
    });
  });
};

export const login = (username, password) => dispatch => {
  // Headers
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  // Request Body
  const body = JSON.stringify({ username, password });

  axios.post("http://localhost:8000/account/api/auth/login", body, config).then(res => {
    dispatch({
      type: LOGIN_SUCCESS,
      payload: res.data
    });
  }).catch(err => {
    dispatch(returnErrors(err.response.data, err.response.status));
    dispatch({
      type: LOGIN_FAIL
    });
  });
};

export const register = ({
  username, password, email, first_name, last_name
  }) => dispatch => {
  // Headers
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
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
    console.log(`Raw response: ${raw}`);
    return raw.json();
  }).then(result => {
    console.log(`Result: ${result}`);
  },
  (error) =>  {
    console.log(`Error in actions.auth.js line 86.\nError ${error}`)
  })
};

export const logout = () => (dispatch, getState) => {
  fetch('http://localhost:8000', null, tokenConfig(getState)).then(raw => {
    console.log(`Raw results: ${raw}`);
    return raw.json();
  }).then(result => {
    console.log(`Result: ${result}`);
    dispatch({
      type: LOGOUT_SUCCESS
    });
  },
  (error) => {
    console.log(`Error in actions.auth.js line 100.\nError:  ${error}`);
  })
};

// Setup config with token
export const tokenConfig = getState => {
  // Get token from state
  const token = getState().auth.token;

  // Headers
  const config = {
    headers: { "Content-Type": "application/json" }
  };

  // If token, add to headers config
  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }

  return config;
};
