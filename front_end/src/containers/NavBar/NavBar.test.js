import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import { NavBar } from './NavBar';

configure({ adapter: new Adapter() });

describe('<NavBar />', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<NavBar />);
    });

    it('should have 2 NavItems', () => {
        expect(wrapper.find('withRouter(navItem)')).toHaveLength(2);
    });

    it('should have Logout link instead of Login if not auth', () => {
        const links = wrapper.find('withRouter(navItem)').map(node => node);
        expect(links[links.length - 1].prop('path')).toEqual('/login');
    });

    it('should have Login link instead of Logout if auth', () => {
        wrapper.setProps({isAuth: true})
        const links = wrapper.find('withRouter(navItem)').map(node => node);
        expect(links[links.length - 1].prop('path')).toEqual('/');
    });
});
