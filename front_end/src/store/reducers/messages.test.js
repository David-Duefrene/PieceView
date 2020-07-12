import messages from './messages';
import * as actions from '../actions/actionTypes';

describe('messages reducer', () => {
    let initialState = {};

    beforeEach(() => {
        initialState = {};
    });

    it('should return initial state', () => {
        expect(messages(undefined, {})).toEqual(initialState);
    });

    it('should return payload as state', () => {
        const action = { payload: { test: 'test' }, type: actions.CREATE_MESSAGE };
        expect(messages(undefined, action)).toEqual({ message: action.payload });
    });
});
