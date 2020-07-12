import * as actions from '../actions/actionTypes';

/**
 * The initial state of the app.
 * @prop {string} token The user's authentication token.
 * @prop {bool} isAuthenticated If the user is authenticated.
 * @prop {bool} isLoading If the app is still loading.
 * @prop {object} user The object representing the app's user.
 */
const initialState = {
    token: localStorage.getItem('token'),
    isAuthenticated: null,
    isLoading: false,
    user: null,
};

/**
 * Dispatches the needed action.
 * @param {object} state The current app state.
 * @param {action} action The action the app needs to dispatch.
 */
export default function (state = initialState, action) {
    switch (action.type) {
    case actions.USER_LOADING:
        return { ...state, isLoading: true };
    case actions.LOGIN_SUCCESS:
    case actions.REGISTER_SUCCESS:
        localStorage.setItem('token', action.payload.token);
        return {
            ...state,
            isAuthenticated: true,
            isLoading: false,
            user: action.payload.user,
        };
    case actions.AUTH_ERROR:
    case actions.LOGIN_FAIL:
    case actions.LOGOUT_SUCCESS:
    case actions.REGISTER_FAIL:
        localStorage.removeItem('token');
        return {
            ...state,
            token: null,
            user: null,
            isAuthenticated: false,
            isLoading: false,
        };
    default: return state;
    }
}
