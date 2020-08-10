import React from 'react';

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import PostStrip from './PostStrip';
import AuthorAvatar from './AuthorAvatar/AuthorAvatar';

configure({ adapter: new Adapter() });

describe('<PostStrip />', () => {
    let wrapper;
    const testUser = {
        first_name: 'fName',
        last_name: 'lName',
        photo_url: '/static/icons/no-picture.jpg',
    };

    beforeEach(() => {
        const date = '01/01/01 00:58';
        wrapper = shallow(<PostStrip user={testUser} title='Test Title' ID={1} created={date} />);
    });

    it('should have 1 card, a title and a created date/time section', () => {
        expect(wrapper.find(AuthorAvatar)).toHaveLength(1);
        expect(wrapper.find('h5')).toHaveLength(1);
        expect(wrapper.find('small')).toHaveLength(1);
    });
});
