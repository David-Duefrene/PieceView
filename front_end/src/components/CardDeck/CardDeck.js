import React, { Fragment } from 'react';
import axios from 'axios';

import store from '../../store';
import PaginateButtons from '../UI/PaginateButtons/PaginateButtons';
import Card from './Card/Card';
import CSS from './CardDeck.module.css';


export class CardDeck extends React.Component {
  state = {
    user_list: [],
    isLoaded: false,
    page_limit: 4,
    page_num: 1,
    user_type: null
  };

  componentDidMount() {
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
        user_type: this.props.user_type,
        page_limit: parseInt(window.innerWidth / 280),
      });      
    });
  }

  /**
   * Gets the first set of cards in user_list.
   */
  first = () => {
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
      this.setState({"page_num": new_page});
    }
  }

  /**
   * Gets the last set of cards in user_list.
   */
  last = () => {
    var new_page = Math.ceil(this.state.user_list.length /
                             this.state.page_limit);
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
            key={i} />
        )
      }
    }
    else { cards = <h1>LOADING!!!</h1>}

    return (
      <Fragment>
        <div className={CSS.CardDeck + ' ' + this.state.user_type}>
          {cards}
        </div>
        <PaginateButtons
          user_type={this.state.user_type}
          first={this.first}
          next={this.next}
          prev={this.previous}
          last={this.last} />
      </Fragment>
    );
  }
}

export default CardDeck;
