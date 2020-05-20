import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { CardDeck } from './CardDeck';
import Card from '../../components/Card/Card';
import PaginateButtons from
    '../../components/UI/PaginateButtons/PaginateButtons';

configure({ adapter: new Adapter() });
jest.mock('../../axios-auth')


describe('CardDeck', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<CardDeck user_type='test-batch' />);
    });

    it('should be loading header if isLoaded is false', () => {
        wrapper.setState({isLoaded: false});
        expect(wrapper.find('h1').text()).toEqual('LOADING!!!');
    });

    it('should load first page by default', async () => {
        const cardNum = wrapper.find('card').map((node) => node.prop('number'));
        expect(cardNum).toEqual([0,1,2]);
    });

    it(`should have a div with a class called CardDeck, 3 Cards and a
        PaginateButtons if loaded`, () => {
        expect(wrapper.find('div.CardDeck')).toHaveLength(1);
        expect(wrapper.find(Card)).toHaveLength(3);
        expect(wrapper.find(PaginateButtons)).toHaveLength(1);
    });

    it('should name card deck after user_type', () => {
        expect(wrapper.find('div.test-batch')).toHaveLength(1);
        wrapper.setState({user_type: 'what'});
        expect(wrapper.find('div.what')).toHaveLength(1);
    });

    it('should move to next page when next is called', () => {
        wrapper.instance().next();
        const cardNum = wrapper.find('card').map((node) => node.prop('number'));
        expect(cardNum).toEqual([3,4,5]);
    });

    it('should move to last page when last is called', () => {
        wrapper.instance().last();
        const cardNum = wrapper.find('card').map((node) => node.prop('number'));
        expect(cardNum).toEqual([7,8,9]);
    });

    it('should move to previous page when previous is called', () => {
        wrapper.instance().last();
        wrapper.instance().previous();
        const cardNum = wrapper.find('card').map((node) => node.prop('number'));
        expect(cardNum).toEqual([6,7,8]);
    });

    it('should move to first page when first is called', () => {
        wrapper.instance().last();
        wrapper.instance().first();
        const cardNum = wrapper.find('card').map((node) => node.prop('number'));
        expect(cardNum).toEqual([0,1,2]);
    });

    it('should not move past last page when next is called', () => {
        wrapper.instance().next();
        wrapper.instance().next();
        wrapper.instance().next();
        const cardNum = wrapper.find('card').map((node) => node.prop('number'));
        expect(cardNum).toEqual([7,8,9]);
    });

    it('should not move past first page when previous is called', () => {
        wrapper.instance().previous();
        const cardNum = wrapper.find('card').map((node) => node.prop('number'));
        expect(cardNum).toEqual([0,1,2]);
    });
});
