import React from 'react';

import axios from 'axios';

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import faker from 'faker';

import { Posts } from './Posts';

configure({ adapter: new Adapter() });
jest.mock('axios');

const testData = {};
testData.count = 20;
testData.next = 'http://test123.com/post/api/postList/?page=2';
testData.previous = null;
testData.results = [];

for (let i = 0; i < 20; i++) {
    const firstName = faker.name.firstName();
    const lastName = faker.name.lastName();
    testData.results.push({
        authors: {
            username: firstName[0] + lastName,
            first_name: firstName,
            last_name: lastName,
            is_staff: false,
            is_active: true,
            date_joined: faker.date.past(),
            photo: faker.image.imageUrl(),
        },
        content: faker.lorem.paragraphs(),
        title: faker.lorem.sentence(),
        created: faker.date.past().toString(),
        get_absolute_url: faker.internet.url(),
    });
}

axios.get.mockImplementation(() => Promise.resolve({ data: testData }));

describe('<Posts />', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Posts />);
    });

    it('should initially show loading', () => {
        wrapper.setState({ isLoaded: false });
        const header = wrapper.find('h1');
        expect(header.text()).toEqual('Posts is loading.');
    });

    it('should allow an unauthenticated user to view active posts', () => {
        const header = wrapper.find('h1');
        expect(header.text()).toEqual('Posts');

        const postStrips = wrapper.find('postStrip').map((node) => node);
        for (let i = 0; i < 20; i++) {
            expect(testData.results[i].title).toEqual(postStrips[i].props().title);
            expect(testData.results[i].content).toEqual(postStrips[i].props().body);
            expect(testData.results[i].created).toEqual(postStrips[i].props().created);
            expect(testData.results[i].authors).toEqual(postStrips[i].props().user);
        }
    });
});
