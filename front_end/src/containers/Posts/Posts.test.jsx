import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import { Posts } from './Posts';

configure({ adapter: new Adapter() });

describe('<Posts />', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Posts />);
    });

    it('should allow an unauthenticated user to view active posts', () => {
        const header = wrapper.find('h1').map((node) => node);
        expect(header).toHaveLength(1);
    });
});
