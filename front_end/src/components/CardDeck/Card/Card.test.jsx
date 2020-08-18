import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';

import { Provider } from 'react-redux';
import thunk from 'redux-thunk';

import { configure, mount } from 'enzyme';
import configureMockStore from 'redux-mock-store';
import Adapter from 'enzyme-adapter-react-16';

import Card from './Card';

configure({ adapter: new Adapter() });
const mockStore = configureMockStore([thunk]);

describe('<Card />', () => {
    let wrapper;

    beforeEach(() => {
        const testUser = {
            first_name: 'fName',
            last_name: 'lName',
            photo: '/static/icons/no-picture.jpg',
        };
        const store = mockStore({ path: 'test' });
        wrapper = mount((
            <Router>
                <Provider store={store}>
                    <Card number={1} userType='test' user={testUser} />
                </Provider>
            </Router>));
    });

    it('should have a CardImage, CardTitle, CardBody,CardFooter, and a Button',
        () => {
            expect(wrapper.find('img.CardImage')).toHaveLength(1);
            expect(wrapper.find('h5.CardTitle').text()).toEqual('fName lName');
            expect(wrapper.find('p.CardBody')).toHaveLength(1);
            expect(wrapper.find('div.CardFooter')).toHaveLength(1);
            expect(wrapper.find('button.Button').map((node) => node)[0].text()).toEqual('Profile');
        });
});
