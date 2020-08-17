import React from 'react';

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import AuthorAvatar from './AuthorAvatar';

configure({ adapter: new Adapter() });

describe('<AuthorAvatar />', () => {
    let wrapper;

    beforeEach(() => {
        const testUser = {
            first_name: 'fName',
            last_name: 'lName',
            photo: '/static/icons/no-picture.jpg',
            get_absolute_url: 'user/1',
        };
        wrapper = shallow(<AuthorAvatar number={1} user={testUser} />);
    });

    it('should have a photo, name, brief text and a profile button', () => {
        expect(wrapper.find('img.AvatarImage')).toHaveLength(1);
        expect(wrapper.find('h5.AvatarTitle').text()).toEqual('fName lName');
        expect(wrapper.find('p.AvatarBody')).toHaveLength(1);
        expect(wrapper.find('div.AvatarFooter')).toHaveLength(1);
        expect(wrapper.find('button.Button').text()).toEqual('Profile');
    });
});
