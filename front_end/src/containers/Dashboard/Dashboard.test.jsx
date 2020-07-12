import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import { Dashboard } from './Dashboard';
import CardDeck from '../../components/CardDeck/CardDeck';

configure({ adapter: new Adapter() });

describe('<Dashboard />', () => {
    let wrapper;
    let user;

    beforeEach(() => {
        user = {
            first_name: 'fName',
            last_name: 'lname',
            photo: 'url/to/photo',
        };
        wrapper = shallow(<Dashboard user={user} />);
    });

    it('should have 2 tabs and a CardDeck', () => {
        expect(wrapper.find('button.NavLink')).toHaveLength(3);
        expect(wrapper.find(CardDeck)).toHaveLength(1);
    });
    it('should have the first tab as active by default', () => {
        const tabs = wrapper.find('button.NavLink').map((node) => node);
        expect(tabs[1].find('.Active')).toHaveLength(1);
    });

    it('should switch to following tab', () => {
        wrapper.find('#Following').find('button').simulate('click');
        const tabs = wrapper.find('button.NavLink').map((node) => node);
        expect(tabs[2].find('.Active')).toHaveLength(1);
        expect(wrapper.find('CardDeck.Following')).toHaveLength(1);
    });

    it('should switch to followers tab', () => {
        wrapper.find('#Following').find('button').simulate('click');
        wrapper.find('#Followers').find('button').simulate('click');
        const tabs = wrapper.find('button.NavLink').map((node) => node);
        expect(tabs[1].find('.Active')).toHaveLength(1);
        expect(wrapper.find('CardDeck.Followers')).toHaveLength(1);
    });
});