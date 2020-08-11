import React, { Component } from 'react';
import PropTypes from 'prop-types';

import axios from '../../axios-auth';
import PaginateButtons from '../UI/PaginateButtons/PaginateButtons';
import Card from './Card/Card';
import CSS from './CardDeck.module.css';

export class CardDeck extends Component {
    /**
    * Displays a set of users.
    * @extends Component
    * @param {string} userType The type of users that the CardDeck is displaying
    * @prop {list: User} userList The list of users the CardDeck is displaying
    * @prop {bool} isLoaded If the page is currently fully loaded
    * @prop {int} pageLimit The max number of cards per page
    * @prop {int} pageNum The current page number
    * @prop {string} userType The type of users that the CardDeck is displaying
    * @prop {error} stateError If there is an error it wil be stored here
    *
    * @example
    * // Returns a users followers list
    * <CardDeck userType='Followers' />
    */
    state = {
        userList: [],
        isLoaded: false,
        maxPages: 0,
        userType: null,
        stateError: null,
        pageNum: 1,
    };

    /**
     * Triggers loadContacts
     */
    componentDidMount() {
        this.loadContacts('account/api/contacts');
    }

    /**
     * Loads the contacts list from the server
     * @param {string} url the url to load contacts from
     * @async
     */
    loadContacts = (url) => {
        axios.get(url).then((result) => {
            const { userType } = this.props;
            this.setState({
                userList: result.data,
                isLoaded: true,
                userType,
                maxPages: Math.ceil(result.data.count / 5),
            });
        }).catch((error) => {
            this.setState({ stateError: error });
        });
    }

    /**
     * Gets the previous page from the server
     */
    previousClicked = () => {
        const { userList, pageNum } = this.state;
        if (userList.previous !== null) {
            this.loadContacts(userList.previous);
            this.setState({ pageNum: pageNum - 1 });
        }
    }

    /**
     * Gets the next page from the server
     */
    nextClicked = () => {
        const { userList, pageNum } = this.state;
        if (userList.next !== null) {
            this.loadContacts(userList.next);
            this.setState({ pageNum: pageNum + 1 });
        }
    }

    /**
     * Gets the first page from the server
     */
    firstClicked = () => {
        this.loadContacts('account/api/contacts');
        this.setState({ pageNum: 1 });
    }

    /**
     * Gets the last page from the server
     */
    lastClicked = () => {
        const { maxPages } = this.state;
        this.loadContacts(`account/api/contacts?page=${maxPages}`);
        this.setState({ pageNum: maxPages });
    }

    /**
     * Renders the CardDeck if the page is loaded, will load a default loading
     * tag if the page has not finished loading.
     */
    render() {
        const {
            stateError, isLoaded, userList, userType, maxPages, pageNum,
        } = this.state;
        if (stateError != null) {
            throw new Error(stateError.toString());
        }
        const cards = [];

        if (isLoaded && userList.count > 0) {
            for (let i = 0; i < userList.results.length; i++) {
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
                <div className={`${CSS.CardDeck} ${userType}`}>{cards}</div>
                <PaginateButtons
                    user_type={userType}
                    pageNum={pageNum}
                    maxPages={maxPages}
                    first={this.firstClicked}
                    next={this.nextClicked}
                    prev={this.previousClicked}
                    last={this.lastClicked}
                />
            </>
        );
    }
}

CardDeck.propTypes = {
    userType: PropTypes.string.isRequired,
};

export default CardDeck;
