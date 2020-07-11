import React from 'react';
import PropTypes from 'prop-types';

import CSS from './Card.module.css';

/**
 * Renders an individual card.
 * @param {int} props.number - The card ID number for the page.
 * @param {string} props.user_type - The user type for the cards.
 */
const card = props => {
    return (
        <div
            className={CSS.Card}
            id={props.user_type + props.number}>
            <img src={props.user['photo_url']} className={CSS.CardImage} />
            <h5 className={CSS.CardTitle}>
                {props.user['first_name'] + ' ' + props.user['last_name']}
            </h5>
            <p className={CSS.CardBody}>Lorem ipsum dolor sit amet, consectetur
            adipiscing elit. Pellentesque dolor enim, facilisis a lectus ut,
            auctor efficitur est. Orci varius natoque penatibus et magnis dis
            parturient montes, nascetur ridiculus mus. Mauris et leo sapien.
            Etiam fringilla ultricies fringilla.</p>
            <div className={CSS.CardFooter}>
            <button
                className={CSS.Button}>Profile</button>
            </div>
        </div>
    );
}

card.propTypes = { number: PropTypes.number, user_type: PropTypes.string }

export default card;
