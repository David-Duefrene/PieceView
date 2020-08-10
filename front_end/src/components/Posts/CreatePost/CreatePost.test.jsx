import React from 'react';

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import axios from '../../../axios-auth';

import CreatePost from './CreatePost';

configure({ adapter: new Adapter() });
jest.mock('../../../axios-auth');

const result = {
    data: {
        status: 'success!!',
        URL: 'test-url',
    },
};

const mockAxios = axios.post.mockImplementation(() => Promise.resolve(result));

describe('<CreatePost />', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<CreatePost history={{ push: () => {} }} />);
    });

    it(`should render a form with a header, Title label, post content header, RichTextEditor tag
        and a button`, () => {
        expect(wrapper.find('form')).toHaveLength(1);
        expect(wrapper.find('h1')).toHaveLength(1);
        expect(wrapper.find('h1').text()).toEqual('Create a post.');
        expect(wrapper.find('label')).toHaveLength(1);
        expect(wrapper.find('label').text()).toEqual('Title:');
        expect(wrapper.find('input')).toHaveLength(1);
        expect(wrapper.find('h3')).toHaveLength(1);
        expect(wrapper.find('h3').text()).toEqual('Post Content');
        // Test for the editor element
        expect(wrapper.find('e')).toHaveLength(1);
        expect(wrapper.find('button')).toHaveLength(1);
    });

    it('should update title into state', () => {
        const titleInput = wrapper.find('input');
        titleInput.simulate('change', { target: { value: 'testTitle' } });
        expect(wrapper.instance().state.title).toEqual('testTitle');
    });

    it('should update the content into the state', () => {
        const contentInput = wrapper.find('e');
        contentInput.simulate('change', 'testContent');
        expect(wrapper.instance().state.content).toEqual('testContent');
    });

    it('should submit form to server', () => {
        const form = wrapper.find('form');

        wrapper.setState({ title: 'testTitle', content: 'testContent' });
        form.simulate('submit', { preventDefault: () => {} });
        expect(mockAxios.mock.calls.length).toBe(1);
    });
});
