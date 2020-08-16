import React from 'react';

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import axios from '../../../axios';
import { Post } from './Post';

configure({ adapter: new Adapter() });
jest.mock('../../../axios');

const result = {
    data: {
        title: 'title',
        content: 'content',
        authors: {
            first_name: 'fName',
            last_name: 'lName',
        },
    },
};

axios.get.mockImplementation(() => Promise.resolve(result));

describe('Post', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Post match={{ params: { pk: '1' } }} />);
    });

    it('should have a post section with a title, author, and content sections with proper results',
        () => {
            expect(wrapper.find('div.Post')).toHaveLength(1);
            expect(wrapper.find('h1.Title')).toHaveLength(1);
            expect(wrapper.find('h1.Title').text()).toEqual(result.data.title);
            expect(wrapper.find('h3.Author')).toHaveLength(1);
            expect(wrapper.find('h3.Author').text()).toEqual(
                `${result.data.authors.first_name} ${result.data.authors.last_name}`,
            );
            expect(wrapper.find('div.Content')).toHaveLength(1);
        });
});
