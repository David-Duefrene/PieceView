import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';

import { Provider } from 'react-redux';
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';

import { configure, mount, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import axios from '../../axios';
import {UserProfile} from './UserProfile';

configure({ adapter: new Adapter() });
const mockStore = configureMockStore([thunk]);
jest.mock('../../axios');

const testUser = {
    first_name: 'fName',
    last_name: 'lName',
    photo: '/static/icons/no-picture.jpg',
    get_absolute_url: 'user/1',
};
axios.get.mockImplementation(() => Promise.resolve({ data: testUser }));

describe('<UserProfile />', () => {
    let wrapper;
    const store = mockStore({ match: { params: { pk: 1 } } });

    beforeEach(() => {

        wrapper = mount((
            <Router>
                <Provider store={store}>
                    <UserProfile match={{ params: { pk: 1 } }} />
                </Provider>
            </Router>
        ));
    });

    it('should have a div named Profile for the user card', () => {
        expect(wrapper.find('div.Profile')).toHaveLength(1);
    });
});
