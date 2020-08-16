import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';

import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';

import { configure, mount } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import LogoutButton from './LogoutButton';

configure({ adapter: new Adapter() });
const mockStore = configureMockStore([thunk]);

describe('<LogoutButton />', () => {
    let wrapper;
    const store = mockStore({});

    beforeEach(() => {
        wrapper = mount(<Router><Provider store={store}><LogoutButton /></Provider></Router>);
    });

    it('should have 1 <a />', () => {
        expect(wrapper.find('a')).toHaveLength(1);
    });
});
