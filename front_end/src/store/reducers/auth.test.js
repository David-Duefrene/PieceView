import auth from './auth';
import * as actions from '../actions/actionTypes';

describe('auth reducer', () => {
    let initialState = {};

    beforeEach(() => {
        initialState = {
            notInitial: false,
            token: null,
            isAuthenticated: null,
            isLoading: false,
            user: null,
        };
    });

    it('should return state with isLoading set true if user is loading', () => {
        const newState = { ...initialState, isLoading: true };
        expect(auth(initialState, { type: actions.USER_LOADING }))
            .toEqual(newState);
    });

    it(`should return state with isAuthenticated set true and user set to
        action.payload if user has successfully loaded`, () => {
        const act = {
            type: actions.REGISTER_SUCCESS, payload: { user: 'test', token: 'testToken' },
        };
        const newState = { ...initialState, ...act.payload, isAuthenticated: true };
        expect(auth(initialState, act)).toEqual(newState);
    });

    it(`should return state with user set to null and isAuthenticated set to
        false if user has successfully logged out`, () => {
        const act = { type: actions.LOGOUT_SUCCESS, payload: 'test' };
        const newState = { ...initialState, token: null, isAuthenticated: false };
        expect(auth(initialState, act)).toEqual(newState);
    });
});
