import React, { Fragment, Component } from 'react';

import axios from '../../axios-auth';
import PaginateButtons from
    '../UI/PaginateButtons/PaginateButtons';
import Card from './Card/Card';
import CSS from './CardDeck.module.css';


export class CardDeck extends Component {
    /**
    * Displays a set of users.
    * @extends Component
    * @param {string} user_type The type of users that the CardDeck is
    *   displaying.
    * @prop {list} user_list The list of users the CardDeck is displaying.
    * @prop {bool} isLoaded If the page is currently fully loaded.
    * @prop {number} pageLimit The max number of cards per page.
    * @prop {number} pageNum The current page number.
    * @prop {string} userType The type of users that the CardDeck is
    *   displaying
    * @example
    * // Returns a users followers list
    * <CardDeck user_type='Followers' />
    */
    state = {
        user_list: [],
        isLoaded: false,
        page_limit: 3,
        page_num: 1,
        user_type: null
    };

    /**
     * Loads the contacts from the server.
     * @async
     */
    componentDidMount() {
    axios.get('account/api/contacts')
        .then( result => {
            this.setState({
                user_list: result.data,
                isLoaded: true,
                user_type: this.props.user_type,
                page_limit: parseInt(window.innerWidth / 280),
            });
        }).catch(error => console.log(error));
    }

    /**
     * Gets the first set of cards in user_list.
     */
    first = () => {
        this.setState({ "page_num": 1 });
    }

    /**
     * Gets the previous set of cards in user_list.
     */
    previous = () => {
        const new_page = this.state.page_num - 1;
        if (new_page < 1) {
            this.first();
        }
        else {
            this.setState({"page_num": new_page});
        }
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

    /**
     * Ensures the page does not try and access and users that are not
     * available.
     */
    pageBoundsCheck = () => {
        let min = (this.state.page_num) * this.state.page_limit;
        if (min >= this.state.user_list.length) {
            min = this.state.user_list.length - this.state.page_limit;
        }
        else { min = min - this.state.page_limit };

        const max = min + this.state.page_limit;
        return { min: min, max: max };
    }

    /**
     * Renders the CardDeck if the page is loaded, will load a default loading
     * tag if the page has not finished loading.
     */
    render() {
        const cards = [];
        if (this.state.isLoaded && this.state.user_list.length > 0) {
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
        else if (!this.state.isLoaded) {
            cards.push(<h1 key='1'>LOADING!!!</h1>)
        }
        else if (this.state.user_type === 'followers') {
            cards.push(<h1>You have no followers.</h1>)
        }
        else if (this.state.user_type === 'following') {
            cards.push(<h1>You are not following anyone.</h1>)
        }
        else { cards.push(<h1>You are not following anyone.</h1>) }

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
