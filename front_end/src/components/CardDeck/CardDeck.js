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
    const rstate = store.getState();
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
  first = () => { this.setState({"page_num": 1}) };

  /**
   * Gets the previous set of cards in user_list.
   */
  previous = () => {
    const new_page = this.state.page_num - 1;
    if (new_page < 1) { this.first() }
    else { this.setState({"page_num": new_page}) }
  }

  /**
   * Gets the next set of cards in user_list.
   */
  next = () => {
    const new_page = this.state.page_num + 1;
    if (new_page * this.state.page_num >= this.state.user_list.length) {
      this.last();
    }
    else { this.setState({"page_num": new_page}) };
  }

  /**
   * Gets the last set of cards in user_list.
   */
  last = () => {
    const new_page = Math.ceil(this.state.user_list.length /
                             this.state.page_limit);
    this.setState({"page_num": new_page});
  }

  pageBoundsCheck = () => {
    let min = (this.state.page_num) * this.state.page_limit;
    if (min >= this.state.user_list.length) {
      min = this.state.user_list.length - this.state.page_limit;
    }
    else { min = min - this.state.page_limit };

    const max = min + this.state.page_limit;
    return {min: min, max: max};
  }

  /**
   * Renders the class.
   */
  render() {
    const cards = [];

    if (this.state.isLoaded) {
      const bounds = this.pageBoundsCheck();
      for (let i = bounds['min']; i < bounds['max']; i++) {
        cards.push(
          <Card
            number={i}
            user={this.state.user_list[i]}
            user_type={this.state.user_type}
            key={i} />
        );
      }
    }
    else { cards.push(<h1>LOADING!!!</h1>) };

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
