import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';

import { Provider } from 'react-redux';
import { configure, mount } from 'enzyme';
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import Adapter from 'enzyme-adapter-react-16';

import NavBar from './NavBar';
import LogoutButton from '../../components/UI/NavItem/LogoutButton/LogoutButton';

configure({ adapter: new Adapter() });
const mockStore = configureMockStore([thunk]);

describe('<NavBar />', () => {
    let wrapper;
    const store = mockStore({
        auth: { isAuthenticated: false },
    });

    beforeEach(() => {
        wrapper = mount(
            <Router>
                <Provider store={store}>
                    <NavBar />
                </Provider>
            </Router>,
        );
    });

    it('should have 3 NavItems', () => {
        expect(wrapper.find('withRouter(navItem)')).toHaveLength(3);
    });

    it('should have Register and Login links if user not authenticated', () => {
        const links = wrapper.find('withRouter(navItem)').map((node) => node);
        expect(links[links.length - 1].prop('path')).toEqual('/login');
        expect(links[links.length - 2].prop('path')).toEqual('/register');
    });

    it('should have Dashboard and Logout links if user is authenticated', () => {
        const authStore = mockStore({
            auth: { isAuthenticated: true },
        });
        wrapper = mount(
            <Router>
                <Provider store={authStore}>
                    <NavBar />
                </Provider>
            </Router>,
        );
        const button = wrapper.find(LogoutButton);
        const links = wrapper.find('withRouter(navItem)').map((node) => node);

        expect(links[links.length - 1].prop('path')).toEqual('/dashboard');
        expect(button).toHaveLength(1);
    });
});
