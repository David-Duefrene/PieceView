import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import LogoutButton from './LogoutButton.js';


configure({ adapter: new Adapter() });

describe('<LogoutButton />', () => {
    let wrapper;

    beforeEach(() => {
        const props = {
            logoutReducer: () => {}
        };
        wrapper = shallow(<LogoutButton {...props} />);
    });

    it('should have 1 <a />', () => {
        expect(wrapper.find('a')).toHaveLength(1);
    });

    it('should have onClick property of test', () => {
        expect(wrapper.find('a')).toHaveLength(1);
    });
});
