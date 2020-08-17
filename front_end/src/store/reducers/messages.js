import * as actions from '../actions/actionTypes';

const initialState = {};

export default function (state = initialState, action) {
    switch (action.type) {
    case actions.CREATE_MESSAGE:
        return { ...state, message: action.payload };
    case actions.DELETE_MESSAGE:
        return { ...state, message: {} };
    default: return state;
    }
}
