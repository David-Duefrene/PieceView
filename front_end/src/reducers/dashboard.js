import { GET_DASHBOARD } from '../actions/types.js';

const initialState = {
  dashboard: []
}

export default function(state=initialState, action) {
  switch(action.type) {
    case GET_DASHBOARD:
      return {
        ...state,
      }
      default:
      return state;
  }
}
