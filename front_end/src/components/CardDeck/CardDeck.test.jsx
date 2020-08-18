import React from 'react';

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import { CardDeck } from './CardDeck';
import Card from './Card/Card';
import PaginateButtons from '../UI/PaginateButtons/PaginateButtons';

configure({ adapter: new Adapter() });
jest.mock('../../axios-auth');

describe('CardDeck', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<CardDeck userType='test-batch' />);
    });

    it(`should have a div with a class called CardDeck, 10 Cards and a
        PaginateButtons if loaded`, () => {
        expect(wrapper.find('div.CardDeck')).toHaveLength(1);
        expect(wrapper.find(Card)).toHaveLength(10);
        expect(wrapper.find(PaginateButtons)).toHaveLength(1);
    });

    it('should name card deck after user_type', () => {
        expect(wrapper.find('div.test-batch')).toHaveLength(1);
    });
});
