import React from 'react';
import PropTypes from 'prop-types';

import CSS from './AuthorAvatar.module.css';

/**
 * Renders an individual card.
 * @param {int} props.number - The card ID number for the page
 * @param {string} props.user.first_name - The user's first name
 * @param {string} props.user.last_name - The user's last name
 * @param {string} props.user.photo - The user's phot url
 */
const authorAvatar = (props) => {
    const { number, user } = props;
    // set default photo
    if (user.photo == null) { user.photo = '/static/icons/no-picture.jpg'; }

    return (
        <div className={CSS.Avatar} id={number}>
            <img src={user.photo} alt='' className={CSS.AvatarImage} />
            <h5 className={CSS.AvatarTitle}>
                {`${user.first_name} ${user.last_name}`}
            </h5>
            <p className={CSS.AvatarBody}>
                Short statement here
            </p>
            <div className={CSS.AvatarFooter}>
                <button type='button' className={CSS.Button}>
                    Profile
                </button>
            </div>
        </div>
    );
};

authorAvatar.propTypes = {
    number: PropTypes.number.isRequired,
    user: PropTypes.shape({
        first_name: PropTypes.string.isRequired,
        last_name: PropTypes.string.isRequired,
        photo: PropTypes.string,
    }).isRequired,
};

export default authorAvatar;
