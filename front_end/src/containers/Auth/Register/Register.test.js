import React from 'react';

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import { Register } from './Register';
import Button from '../../../components/UI/Button/Button'

configure({ adapter: new Adapter() });


describe('<Register />', () => {
    let wrapper;
    const mockRegister = jest.fn();
    const expectedLabels = ['username', 'email', 'password', 'password2']

    beforeEach(() => {

        wrapper = shallow(<Register register={mockRegister} />);
    });

    it('should render a registration form with 4 separate fields', () => {
        expect(wrapper.find('form')).toHaveLength(1);
        expect(wrapper.find('input.input')).toHaveLength(4);
        expect(wrapper.find('button')).toHaveLength(1);
    });

    it(`should have 4 label tags, username, email, password, password2`, () => {
        const labels = wrapper.find('label').map(node => node.find('label'));

        expect(labels).toHaveLength(4);
        for (let index = 0; index < labels.length; index++) {
            expect(labels[index].text()).toEqual(expectedLabels[index]);
        }

    });

    it('should have 4 inputs that update their value into the state', () => {
        const inputs = wrapper.find('input').map(node => node);
        expect(inputs).toHaveLength(4);

        for (let index = 0; index < inputs.length; index++) {
            wrapper.instance().onChange({ target: {
                name: expectedLabels[index], value: expectedLabels[index]}})
            expect(
                wrapper.instance().state['form'][expectedLabels[index]]['value']
            ).toEqual(expectedLabels[index]);
        }
    });

    it(`should have a submit button that fires onSubmit`, () => {
        // mockRegister should not been called at this point, if it has we
        // are firing the form submit prematurely.
        expect(mockRegister.mock.calls.length).toBe(0);
        expect(wrapper.find(Button)).toHaveLength(1);
        wrapper.instance().onSubmit({
            preventDefault: () => {},
        });
        expect(mockRegister.mock.calls.length).toBe(1);
    });
});
