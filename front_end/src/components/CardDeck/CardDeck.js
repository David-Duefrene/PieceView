import React from 'react';
import axios from 'axios';

import $ from "jquery";

import store from '../../store';
import PaginateButtons from '../UI/PaginateButtons/PaginateButtons';
import Card from './Card/Card';


export class UserCards extends React.Component {
  state = {
    user_list: [],
    isLoaded: false,
    page_limit: 4,
    page_num: 1,
    user_type: null
  };

  /**
   * Constructor
   * @param props.user_type - The user type for this instance.
   */
  constructor(props) {
    super(props);
    // Headers
    const rstate = store.getState()
    const config = {
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Token ${rstate.auth['token']}`
      }
    };

    axios.get('http://localhost:8000/account/api/contacts', config)
    .then( result => {
      this.setState({
        user_list: result.data,
        isLoaded: true,
        user_type: props.user_type});
      this.change(0);
    });
  }

  getFollowers(config) {
    axios.get('http://localhost:8000/account/api/contacts', config)
    .then( result => {
      this.setState({isLoaded: true,  user_list: result.data});
    });
  }

  /**
   * Changes the cards to new set of users.
   * @param start - the index in the user_list the loop should start at.
   */
  change = (start) => {
    for (var i = 0; i < this.state.page_limit; i++) {
      $('#' + this.state.user_type + i + ' img.card-img-top').attr("src",
        this.state.user_list[i + start]['photo_url']);
      $('#' + this.state.user_type + i + ' div.card-footer a.btn').attr("href",
        this.state.user_list[i + start]["get_absolute_url"]);
      $('#' + this.state.user_type + i + ' .card-body .card-title').text(
        this.state.user_list[i + start]["first_name"] + " " +
          this.state.user_list[i + start]["last_name"]);
    }
  }  

  /**
   * Gets the first set of cards in user_list.
   */
  first = () => {
    this.change(0);
    this.setState({"page_num": 1});
  }

  /**
   * Gets the previous set of cards in user_list.
   */
  previous = () => {
    var new_page = this.state.page_num - 1;
    if (new_page < 1) { this.first(); }
    else {
      this.setState({"page_num": new_page});
      new_page -= 1;
      this.change(new_page * this.state.page_limit);
    }
  }

  /**
   * Gets the next set of cards in user_list.
   */
  next = () => {
    var new_page = this.state.page_num + 1;
    if (new_page * this.state.page_num >=
        this.state.user_list.length) {
      this.last();
    }
    else {
      this.change(this.state.page_num * this.state.page_limit);
      this.setState({"page_num": new_page});
    }
  }

  /**
   * Gets the last set of cards in user_list.
   */
  last = () => {
    var new_page = Math.ceil(this.state.user_list.length /
                             this.state.page_limit);
    this.change(this.state.user_list.length - this.state.page_limit);
    this.setState({"page_num": new_page});
  }

  /**
   * Renders the class.
   */
  render() {
    var cards = []

    if (this.state.isLoaded) {
      let temp = (this.state.page_num - 1) * this.state.page_limit;
      const max = temp + this.state.page_limit;

      for (var i = temp; i < max; i++) {
        cards.push(
          <Card
            number={i}
            user={this.state.user_list[i]}
            user_type={this.state.user_type}
            key={i} />)
      }
    }
    else { cards = <h1>LOADING!!!</h1>}

    return (
      <div className="d-flex tab-content col-12">
        <div className={"card-deck " + this.state.user_type}>
          {cards}
        </div>
        <div className="d-flex deck-footer">
          <PaginateButtons user_type={this.state.user_type} />
        </div>
      </div>
    );
  }

  componentWillUnmount() {
    this.setState({isLoaded: false});
  }
}

  /**
  * Card Deck itself.
  * @param props.user_type - type of user to display.
  */
function CardDeck(props) {
  return (
    <div className="CardDeckApp">
      <UserCards user_type={props.user_type} />
    </div>
  );
}

export default CardDeck;
