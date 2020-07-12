import React from 'react';
// import axios from 'axios';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import Card from './Card';

configure({ adapter: new Adapter() });

describe('<Card />', () => {
    let wrapper;

    beforeEach(() => {
        const testUser = {
            first_name: 'fName',
            last_name: 'lName',
            photo: '/static/icons/no-picture.jpg',
        };
        wrapper = shallow(<Card number={1} userType='test' user={testUser} />);
    });

    it('should have a CardImage, CardTitle, CardBody,CardFooter, and a Button',
        () => {
            expect(wrapper.find('img.CardImage')).toHaveLength(1);
            expect(wrapper.find('h5.CardTitle').text()).toEqual('fName lName');
            expect(wrapper.find('p.CardBody')).toHaveLength(1);
            expect(wrapper.find('div.CardFooter')).toHaveLength(1);
            expect(wrapper.find('button.Button').text()).toEqual('Profile');
        });
});
