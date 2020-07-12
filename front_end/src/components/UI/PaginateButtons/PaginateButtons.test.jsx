import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import PaginateButtons from './PaginateButtons';

configure({ adapter: new Adapter() });

describe('<PaginateButtons />', () => {
    let wrapper;
    let test;

    beforeEach(() => {
        test = false;
        const first = () => { test = true; };
        const last = () => { test = true; };
        const prev = () => { test = true; };
        const next = () => { test = true; };
        wrapper = shallow(
            <PaginateButtons
                first={first}
                last={last}
                prev={prev}
                next={next}
                userType='test'
            />,
        );
    });

    it(`should have 4 buttons with class named Button and 1 button with class
          named PageNum`, () => {
        expect(wrapper.find('button.Button')).toHaveLength(4);
        expect(wrapper.find('button.PageNum')).toHaveLength(1);
    });

    it('should call first function when first page button is clicked', () => {
        const buttons = wrapper.find('button.Button').map((node) => node);
        buttons[0].simulate('click');
        expect(test).toBeTruthy();
    });

    it(
        'should call previous function when previous page button is clicked',
        () => {
            let passed = false;
            wrapper.setProps({ prev: () => { passed = true; } });
            const buttons = wrapper.find('button.Button').map((node) => node);
            buttons[1].simulate('click');
            expect(passed).toBeTruthy();
        },
    );

    it('should call next function when next page button is clicked', () => {
        let passed = false;
        wrapper.setProps({ next: () => { passed = true; } });
        const buttons = wrapper.find('button.Button').map((node) => node);
        buttons[2].simulate('click');
        expect(passed).toBeTruthy();
    });

    it('should call last function when last page button is clicked', () => {
        let passed = false;
        wrapper.setProps({ last: () => { passed = true; } });
        const buttons = wrapper.find('button.Button').map((node) => node);
        buttons[3].simulate('click');
        expect(passed).toBeTruthy();
    });

    it('should have pageNum class append user_type', () => {
        wrapper.setProps({ userType: 'test' });
        expect(wrapper.find('span.current-page-test')).toHaveLength(1);
    });
});