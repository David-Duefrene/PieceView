import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { NavLink } from 'react-router-dom';

import { NavItemTest } from './NavItem';

configure({ adapter: new Adapter() });

describe('<NavItem />', () => {
    let wrapper;

    beforeEach(() => {
        const match = { url: '/test' };
        wrapper = shallow(<NavItemTest match={match} path='/test' exact>Test</NavItemTest>);
    });

    it('should have 1 NavLink', () => {
        expect(wrapper.find(NavLink)).toHaveLength(1);
    });

    it(`should not have an have an active class if current URL does not match
        destination path`, () => {
        wrapper.setProps({ path: 'different' });
        expect(wrapper.find('.Active')).toHaveLength(0);
    });
});
