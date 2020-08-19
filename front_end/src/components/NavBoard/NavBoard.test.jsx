import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import NavBoard from './NavBoard';

configure({ adapter: new Adapter() });

describe('<NavBoard />', () => {
    let wrapper;
    let boards = null;

    beforeEach(() => {
        boards = [
            {
                name: 'Test1',
                element: <h1>Test 1</h1>,
            },
            {
                name: 'Test2',
                element: <h1>Test 2</h1>,
            },
        ];
        wrapper = shallow(<NavBoard boards={boards} />);
    });

    it('should render 2 buttons and a h1 by default', () => {
        expect(wrapper.find('button')).toHaveLength(2);
        expect(wrapper.find('h1')).toHaveLength(1);
    });

    it('should render 1st tab by default', () => {
        const button = wrapper.find('.Active');
        expect(button.text()).toEqual(boards[0].name);
    });

    it('should render 2nd tab if clicked', () => {
        expect(wrapper.find('button')).toHaveLength(2);
        const buttons = wrapper.find('button').map((node) => node);
        buttons[1].simulate('click');
        expect(wrapper.find('.Active').text()).toEqual(boards[1].name);
        expect(wrapper.find('h1').text()).toEqual('Test 2');
    });
});
