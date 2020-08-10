import React from 'react';
import PropTypes from 'prop-types';

import CSS from './PostStrip.module.css';
import AuthorAvatar from './AuthorAvatar/AuthorAvatar';

/**
 * Renders the post strip with basic info of the post
 * @param {int} props.ID - The card ID number for the post and card
 * @param {string} props.title The title of the post
 * @param {string} props.body The body of the post
 * @param {string} props.user.first_name - The user's first name
 * @param {string} props.user.last_name - The user's last name
 * @param {string} props.user.photo - The user's phot url
 */
const postStrip = (props) => {
    const {
        ID, title, user, created, body,
    } = props;
    return (
        <div className={CSS.PostList}>
            <AuthorAvatar className={CSS.Card} number={ID} user={user} />
            <div className={CSS.Post}>
                <h5>{title}</h5>
                <p>{body}</p>
                <small>{created}</small>
            </div>
        </div>
    );
};

postStrip.propTypes = {
    ID: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    body: PropTypes.string.isRequired,
    created: PropTypes.string.isRequired,
    user: PropTypes.shape({
        first_name: PropTypes.string.isRequired,
        last_name: PropTypes.string.isRequired,
        photo: PropTypes.string,
    }).isRequired,
};

export default postStrip;
