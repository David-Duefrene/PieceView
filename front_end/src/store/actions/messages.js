import * as actions from './actionTypes';


/**
 * Returns any Error our application may run into.
 * @param {string} msg The error message itself.
 * @param {string} status The status code.
 */
export const returnErrors = ( msg, status ) => {
    return {
        type: actions.GET_ERRORS,
        payload: { msg, status }
    };
};
