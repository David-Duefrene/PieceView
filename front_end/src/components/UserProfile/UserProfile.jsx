import React, { Component } from 'react';
import { withRouter } from 'react-router';
import PropTypes from 'prop-types';

import Card from '../CardDeck/Card/Card';
import axios from '../../axios';
import CSS from './UserProfile.module.css';

/**
 * Renders a user profile for an individual user
 * @param {string} match.params.pk The primary key for the user
 * @prop {object} user The current user being displayed
 * @prop {bool} isLoaded If the current page has loaded
 */
export class UserProfile extends Component {
    state = {
        user: null,
        isLoaded: false,
    };

    componentDidMount() {
        const { match } = this.props;
        axios.get(`account/api/account/edit/${match.params.pk}`).then((result) => {
            this.setState({
                isLoaded: true,
                user: result.data,
            });
        }).catch((error) => Error(error));
    }

    render() {
        const { isLoaded, user } = this.state;

        return (
            <div className={CSS.Profile}>
                { isLoaded ? <Card user={user} /> : (<h1>Loading!!!</h1>)}
            </div>
        );
    }
}

UserProfile.propTypes = {
    match: PropTypes.shape({
        params: PropTypes.shape({
            pk: PropTypes.number.isRequired,
        }).isRequired,
    }).isRequired,
};

export default withRouter(UserProfile);
