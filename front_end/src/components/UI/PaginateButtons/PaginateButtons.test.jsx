import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import PaginateButtons from './PaginateButtons';

configure({ adapter: new Adapter() });

describe('<PaginateButtons />', () => {
    let wrapper;
    const first = jest.fn();
    const last = jest.fn();
    const prev = jest.fn();
    const next = jest.fn();

    beforeEach(() => {
        wrapper = shallow(
            <PaginateButtons
                pageNum={1}
                maxPages={5}
                first={first}
                last={last}
                prev={prev}
                next={next}
            />,
        );
    });

    it(`should have 4 buttons with class named Button and 1 button with class named PageNum`,
        () => {
            expect(wrapper.find('button.Button')).toHaveLength(4);
            expect(wrapper.find('button.PageNum')).toHaveLength(1);
        });

    it('should call first function when first page button is clicked', () => {
        const buttons = wrapper.find('button.Button').map((node) => node);
        buttons[0].simulate('click');

        expect(first.mock.calls.length).toBe(1);
    });

    it('should call previous function when previous page button is clicked', () => {
        const buttons = wrapper.find('button.Button').map((node) => node);
        buttons[1].simulate('click');

        expect(prev.mock.calls.length).toBe(1);
    });

    it('should call next function when next page button is clicked', () => {
        const buttons = wrapper.find('button.Button').map((node) => node);
        buttons[2].simulate('click');

        expect(next.mock.calls.length).toBe(1);
    });

    it('should call last function when last page button is clicked', () => {
        const buttons = wrapper.find('button.Button').map((node) => node);
        buttons[3].simulate('click');

        expect(last.mock.calls.length).toBe(1);
    });

    it('should have a page number and max pages button', () => {
        const button = wrapper.find('button.PageNum');
        expect(button.text()).toEqual('Page 1 of 5');
    });
});
