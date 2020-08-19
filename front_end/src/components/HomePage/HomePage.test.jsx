import React from 'react';

import { Provider } from 'react-redux';
import { configure, mount } from 'enzyme';
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import Adapter from 'enzyme-adapter-react-16';

import HomePage from './HomePage';
import NavBoard from '../NavBoard/NavBoard';

configure({ adapter: new Adapter() });
const mockStore = configureMockStore([thunk]);

describe('<HomePage />', () => {
    let wrapper;
    const store = mockStore({
        auth: { isAuthenticated: false },
    });

    beforeEach(() => {
        wrapper = mount(<Provider store={store}><HomePage /></Provider>);
    });

    it('should have 1 Navboard', () => {
        expect(wrapper.find(NavBoard)).toHaveLength(1);
    });

    it('should have 1 NavItem if user is not authenticated', () => {
        expect(wrapper.find('.NavItem')).toHaveLength(1);
    });

    it('should have 2 NavItems if user is authenticated', () => {
        const authStore = mockStore({
            auth: { isAuthenticated: true },
        });
        wrapper = mount(<Provider store={authStore}><HomePage /></Provider>);
        expect(wrapper.find('.NavItem')).toHaveLength(2);
    });
});
