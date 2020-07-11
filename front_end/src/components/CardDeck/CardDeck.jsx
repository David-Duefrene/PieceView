import React, { Component } from 'react';
import PropTypes from 'prop-types';

import axios from '../../axios-auth';
import PaginateButtons from
    '../UI/PaginateButtons/PaginateButtons';
import Card from './Card/Card';
import CSS from './CardDeck.module.css';

export class CardDeck extends Component {
    /**
    * Displays a set of users.
    * @extends Component
    * @param {string} userType The type of users that the CardDeck is
    *   displaying.
    * @prop {list} userList The list of users the CardDeck is displaying.
    * @prop {bool} isLoaded If the page is currently fully loaded.
    * @prop {number} pageLimit The max number of cards per page.
    * @prop {number} pageNum The current page number.
    * @prop {string} userType The type of users that the CardDeck is
    *   displaying
    * @example
    * // Returns a users followers list
    * <CardDeck userType='Followers' />
    */
    state = {
        userList: [],
        isLoaded: false,
        pageLimit: 3,
        pageNum: 1,
        userType: null,
        stateError: null,
    };

    /**
     * Loads the contacts from the server.
     * @async
     */
    componentDidMount() {
        axios.get('account/api/contacts').then((result) => {
            const { userType } = this.props;
            this.setState({
                userList: result.data,
                isLoaded: true,
                userType,
                pageLimit: parseInt(window.innerWidth / 280, 10),
            });
        }).catch((error) => {
            this.setState({ stateError: error });
        });
    }

    /**
     * Gets the first set of cards in userList.
     */
    first = () => {
        this.setState({ pageNum: 1 });
    }

    /**
     * Gets the previous set of cards in userList.
     */
    previous = () => {
        const { state } = this.state;
        const { newPage } = state.pageNum - 1;
        if (newPage < 1) {
            this.first();
        } else {
            this.setState({ pageNum: newPage });
        }
    }

    /**
     * Gets the next set of cards in userList.
     */
    next = () => {
        const { state } = this.state;
        const { newPage } = state.pageNum + 1;
        if (newPage * state.pageNum >= state.userList.length) {
            this.last();
        } else { this.setState({ pageNum: newPage }); }
    }

    /**
     * Gets the last set of cards in userList.
     */
    last = () => {
        const { state } = this.state;
        const newPage = Math.ceil(state.userList.length / state.pageLimit);
        this.setState({ pageNum: newPage });
    }

    /**
     * Ensures the page does not try and access and users that are not
     * available.
     */
    pageBoundsCheck = () => {
        const { state } = this.state;
        let min = (state.pageNum) * state.pageLimit;
        if (min >= state.userList.length) {
            min = state.userList.length - state.pageLimit;
        } else { min -= state.pageLimit; }

        const max = min + state.pageLimit;
        return { min, max };
    }

    /**
     * Renders the CardDeck if the page is loaded, will load a default loading
     * tag if the page has not finished loading.
     */
    render() {
        const {
            stateError, isLoaded, userList, userType,
        } = this.state;
        if (stateError != null) {
            return (
                <h1>
                    Error:
                    {stateError}
                </h1>
            );
        }
        const cards = [];

        if (isLoaded && userList.count > 0) {
            for (let i = 0; i < userList.count; i++) {
                cards.push(
                    <Card
                        number={i}
                        user={userList.results[i]}
                        user_type={userType}
                        key={i}
                    />,
                );
            }
        } else if (!isLoaded) {
            cards.push(<h1 key='1'>LOADING!!!</h1>);
        } else if (userType === 'followers') {
            cards.push(<h1>You have no followers.</h1>);
        } else if (userType === 'following') {
            cards.push(<h1>You are not following anyone.</h1>);
        }

        return (
            <>
                <div className={`${CSS.CardDeck} ${userType}`}>
                    {cards}
                </div>
                <PaginateButtons
                    user_type={userType}
                    first={this.first}
                    next={this.next}
                    prev={this.previous}
                    last={this.last}
                />
            </>
        );
    }
}

CardDeck.propTypes = {
    userType: PropTypes.string.isRequired,
};

export default CardDeck;
