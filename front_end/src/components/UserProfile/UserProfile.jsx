import React, { Component } from 'react';
import { withRouter } from 'react-router';
import PropTypes from 'prop-types';
import dotenv from 'dotenv';

import axios from '../../axios';
import CSS from './UserProfile.module.css';

const config = dotenv.config();

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
            <div>
                { isLoaded ? (
                    <div className={CSS.UserProfile}>
                        <h1>{user.username}</h1>
                        <h3>{`Name: ${user.first_name} ${user.last_name}`}</h3>
                        <img src={`${process.env.REACT_APP_API_URL}${user.photo_url}`} />
                        <p>{user.biography}</p>
                    </div>
                ) : (<h1>Loading!!!</h1>)}
            </div>
        );
    }
}

export default withRouter(UserProfile);
