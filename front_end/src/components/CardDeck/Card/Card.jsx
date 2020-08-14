import React, { useState } from 'react';
import PropTypes from 'prop-types';

import axios from '../../../axios-auth';
import CSS from './Card.module.css';

/**
 * Renders an individual card.
 * @param {int} number - The card ID number for the page
 * @param {string} userType - The user type for the cards
 * @param {func} contact - The contact function
 * @param {bool} isFollowed - If the user is followed
 * @param {string} user.first_name - The user's first name
 * @param {string} user.last_name - The user's last name
 * @param {string} user.photo - The user's phot url
 */
const Card = (props) => {
    const {
        userType, number, user, following,
    } = props;
    const [buttonText, setButtonText] = useState(following ? 'unfollow' : 'follow');
    // set default photo
    if (user.photo == null) { user.photo = '/static/icons/no-picture.jpg'; }

    return (
        <div className={CSS.Card} id={userType + number}>
            <img src={user.photo} alt='' className={CSS.CardImage} />
            <h5 className={CSS.CardTitle}>
                {`${user.first_name} ${user.last_name}`}
            </h5>
            <p className={CSS.CardBody}>{user.biography}</p>
            <div className={CSS.CardFooter}>
                <button type='button' className={CSS.Button}>Profile</button>
                <button
                    type='button'
                    className={CSS.Button}
                    onClick={() => {
                        axios.post(
                            'http://localhost:8000/account/api/contacts',
                            { action: buttonText, username: user.username },
                        ).then(() => {
                            setButtonText(buttonText === 'follow' ? 'unfollow' : 'follow');
                        }).catch((error) => console.log(error));
                    }}
                >
                    {buttonText}
                </button>
            </div>
        </div>
    );
};

Card.propTypes = {
    number: PropTypes.number.isRequired,
    userType: PropTypes.string.isRequired,
    following: PropTypes.bool.isRequired,
    user: PropTypes.shape({
        username: PropTypes.string.isRequired,
        first_name: PropTypes.string.isRequired,
        last_name: PropTypes.string.isRequired,
        biography: PropTypes.string.isRequired,
        photo: PropTypes.string,
    }).isRequired,
};

export default Card;
