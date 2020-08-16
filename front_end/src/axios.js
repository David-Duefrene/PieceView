import axios from 'axios';
import dotenv from 'dotenv';

const config = dotenv.config();

const instance = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default instance;
