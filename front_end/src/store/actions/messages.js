import * as actions from "./actionTypes";

export const returnErrors = ( msg, status ) => {
    return {
        type: actions.GET_ERRORS,
        payload: { msg, status }
    };
};
