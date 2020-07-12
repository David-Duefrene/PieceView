import * as actions from '../actions/actionTypes';

const initialState = {};

export default function (state = initialState, action) {
    switch (action.type) {
    case actions.CREATE_MESSAGE:
        return { ...state, message: action.payload };
    default: return state;
    }
}
