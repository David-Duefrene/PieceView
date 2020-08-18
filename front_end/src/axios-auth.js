import axios from 'axios';
import dotenv from 'dotenv';

import store from './store';

const config = dotenv.config();

const state = store.getState();

const instance = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${state.auth.token}`,
    },
});

export default instance;
