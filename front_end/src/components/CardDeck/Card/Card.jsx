import React from 'react';
import PropTypes from 'prop-types';

import CSS from './Card.module.css';

/**
 * Renders an individual card.
 * @param {int} props.number - The card ID number for the page
 * @param {string} props.userType - The user type for the cards
 * @param {string} props.user.first_name - The user's first name
 * @param {string} props.user.last_name - The user's last name
 * @param {string} props.user.photo_url - The user's phot url
 */
const card = (props) => {
    const { userType, number, user } = props;
    return (
        <div className={CSS.Card} id={userType + number}>
            <img src={user.photo_url} alt='' className={CSS.CardImage} />
            <h5 className={CSS.CardTitle}>
                {`${user.first_name} ${user.last_name}`}
            </h5>
            <p className={CSS.CardBody}>
                Lorem ipsum dolor sit amet, consectetur
                adipiscing elit. Pellentesque dolor enim, facilisis a lectus ut,
                auctor efficitur est. Orci varius natoque penatibus et magnis dis
                parturient montes, nascetur ridiculus mus. Mauris et leo sapien.
                Etiam fringilla ultricies fringilla.
            </p>
            <div className={CSS.CardFooter}>
                <button type='button' className={CSS.Button}>
                    Profile
                </button>
            </div>
        </div>
    );
};

card.propTypes = {
    number: PropTypes.number.isRequired,
    userType: PropTypes.string.isRequired,
    user: PropTypes.shape({
        first_name: PropTypes.string.isRequired,
        last_name: PropTypes.string.isRequired,
        photo_url: PropTypes.string.isRequired,
    }).isRequired,
};

export default card;
