import axios from 'axios';

import store from './store';

const state = store.getState();

const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    headers: {
        "Content-Type": "application/json",
        "Authorization": `Token ${state.auth['token']}`
    }
});

export default instance;
