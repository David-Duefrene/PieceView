import React from 'react';
import PropTypes from 'prop-types';

import CSS from './AuthorAvatar.module.css';

/**
 * Renders an individual card.
 * @param {int} number - The card ID number for the page
 * @param {string} user.first_name - The user's first name
 * @param {string} user.last_name - The user's last name
 * @param {string} user.photo_link - The user's phot url
 */
const authorAvatar = (props) => {
    const { number, user } = props;

    return (
        <div className={CSS.Avatar} id={number}>
            <img src={user.photo_link} alt='' className={CSS.AvatarImage} />
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
        photo_link: PropTypes.string,
    }).isRequired,
};

export default authorAvatar;
