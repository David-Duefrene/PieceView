import React from 'react';
import {configure, shallow} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import {Login} from './Login';

configure({adapter: new Adapter()});

describe('<Login />', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Login />);
    });

    it('should render login form with 2 separate fields', () => {
        expect(wrapper.find('form')).toHaveLength(1);
        expect(wrapper.find('input.input')).toHaveLength(2);
        expect(wrapper.find('button')).toHaveLength(1);
    });
});
