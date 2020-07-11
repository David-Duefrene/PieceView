import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import Button from './Button';
configure({adapter: new Adapter()});


describe('<Button />', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Button type='submit' />);
    });

    it('should have 1 button with the type submit', () => {
        const button = wrapper.find('button');
        expect(button).toHaveLength(1);
    });
});
