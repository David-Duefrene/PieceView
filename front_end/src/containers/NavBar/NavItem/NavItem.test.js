import React from 'react';
import {configure, shallow} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {NavLink} from 'react-router-dom';

import {NavItemTest} from './NavItem';

configure({adapter: new Adapter()});

describe('<NavItem />', () => {
  let wrapper;

  beforeEach(() => {
    const props = {
      match: {
        url: 'test'
      },
      path: 'test'
    };
    wrapper = shallow(<NavItemTest {...props} />);
  });

  it('should have 1 NavLink', () => {
    expect(wrapper.find(NavLink)).toHaveLength(1);
  });

  it('should be active if current URL mathches destination path', () => {
    expect(wrapper.find('.Active')).toHaveLength(1);
  });

    it('should not have an have an active class if current URL does not mathch destination path', () => {
    wrapper.setProps({path: 'diffrent'});
    expect(wrapper.find('.Active')).toHaveLength(0);
  });

});
