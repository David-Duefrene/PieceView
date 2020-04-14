import React from 'react';
import axios from 'axios';
import {configure, shallow} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import {CardDeck} from './CardDeck';
import Card from '../../components/Card/Card';
import PaginateButtons from
  '../../components/UI/PaginateButtons/PaginateButtons';

const data = {
  user_list: [
    {
      "username": "WAnderson",
      "email": "WAnderson@mail.com",
      "photo": null,
      "first_name": "William",
      "last_name": "Anderson",
      "followers": [],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/WAnderson/"
    },
    {
      "username": "CGlover",
      "email": "CGlover@mail.com",
      "photo": null,
      "first_name": "Cynthia",
      "last_name": "Glover",
      "followers": [
        1
      ],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/CGlover/"
    },
    {
      "username": "JPatterson",
      "email": "JPatterson@mail.com",
      "photo": null,
      "first_name": "Jamie",
      "last_name": "Patterson",
      "followers": [
        1
      ],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/JPatterson/"
    },
    {
      "username": "SHansen",
      "email": "SHansen@mail.com",
      "photo": null,
      "first_name": "Sheila",
      "last_name": "Hansen",
      "followers": [],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/SHansen/"
    },
    {
      "username": "JArias",
      "email": "JArias@mail.com",
      "photo": null,
      "first_name": "Jonathan",
      "last_name": "Arias",
      "followers": [],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/JArias/"
    },
    {
      "username": "DTaylor",
      "email": "DTaylor@mail.com",
      "photo": null,
      "first_name": "Daniel",
      "last_name": "Taylor",
      "followers": [],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/DTaylor/"
    },
    {
      "username": "LAcosta",
      "email": "LAcosta@mail.com",
      "photo": null,
      "first_name": "Lisa",
      "last_name": "Acosta",
      "followers": [],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/LAcosta/"
    },
    {
      "username": "WFernandez",
      "email": "WFernandez@mail.com",
      "photo": null,
      "first_name": "William",
      "last_name": "Fernandez",
      "followers": [],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/WFernandez/"
    },
    {
      "username": "JJuarez",
      "email": "JJuarez@mail.com",
      "photo": null,
      "first_name": "John",
      "last_name": "Juarez",
      "followers": [],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/JJuarez/"
    },
    {
      "username": "SMeyer",
      "email": "SMeyer@mail.com",
      "photo": null,
      "first_name": "Sarah",
      "last_name": "Meyer",
      "followers": [],
      "photo_url": "/static/icons/no-picture.jpg",
      "get_absolute_url": "/account/people/SMeyer/"
    }
  ]
};
configure({adapter: new Adapter()});
jest.mock('axios');
axios.get.mockResolvedValue({data: data['user_list']})


describe('CardDeck', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallow(<CardDeck user_type='test-batch' />);
  });

  it('should be loading header if isLoaded is false', async () => {
    wrapper.setState({isLoaded: false});
    expect(wrapper.find('h1').text()).toEqual('LOADING!!!');
  });

  it('should load first page by default', async () => {
    const cardNums = wrapper.find('card').map((node) => node.prop('number'));
    expect(cardNums).toEqual([0,1,2]);
  });

  it('should have a div with a class called CardDeck, 3 Cards and a PaginateButtons if loaded', () => {
    expect(wrapper.find('div.CardDeck')).toHaveLength(1);
    expect(wrapper.find(Card)).toHaveLength(3);
    expect(wrapper.find(PaginateButtons)).toHaveLength(1);
  });

  it('should name card deck after user_type', () => {
    expect(wrapper.find('div.test-batch')).toHaveLength(1);
    wrapper.setState({user_type: 'what'})
    expect(wrapper.find('div.what')).toHaveLength(1);
  });

  it('should move to next page when next is called', () => {
      wrapper.instance().next();
      const cardNums = wrapper.find('card').map((node) => node.prop('number'));
      expect(cardNums).toEqual([3,4,5]);
  });

  it('should move to last page when last is called', () => {
      wrapper.instance().last();
      const cardNums = wrapper.find('card').map((node) => node.prop('number'));
      expect(cardNums).toEqual([7,8,9]);
  });

  it('should move to previous page when previous is called', () => {
      wrapper.instance().last();
      wrapper.instance().previous();
      const cardNums = wrapper.find('card').map((node) => node.prop('number'));
      expect(cardNums).toEqual([6,7,8]);
  });

  it('should move to first page when first is called', () => {
      wrapper.instance().last();
      wrapper.instance().first();
      const cardNums = wrapper.find('card').map((node) => node.prop('number'));
      expect(cardNums).toEqual([0,1,2]);
  });

  it('should not move past last page when next is called', () => {
      wrapper.instance().next();
      wrapper.instance().next();
      wrapper.instance().next();
      const cardNums = wrapper.find('card').map((node) => node.prop('number'));
      expect(cardNums).toEqual([7,8,9]);
  });

  it('should not move past first page when previous is called', () => {
      wrapper.instance().previous();
      const cardNums = wrapper.find('card').map((node) => node.prop('number'));
      expect(cardNums).toEqual([0,1,2]);
  });
});



