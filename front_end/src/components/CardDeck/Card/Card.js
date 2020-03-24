import React from 'react';

/**
 * Renders an individual card.
 * @param {int} props.number - The card ID number for the page.
 * @param {string} props.user_type - The user type for the cards.
 */
function card(props) {
  return (
    <div className="card bg-transparent border-warning"
         id={props.user_type + props.number}>
      <img src="NULL" className="card-img-top" />
      <div className="card-body">
        <h5 className="card-title">
          {props.first_name + ' ' + props.last_name}
        </h5>
        <p className="card-text">Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Pellentesque dolor enim, facilisis a lectus ut,
        auctor efficitur est. Orci varius natoque penatibus et magnis dis
        parturient montes, nascetur ridiculus mus. Mauris et leo sapien.
        Etiam fringilla ultricies fringilla.</p>
      </div>
      <div className="card-footer bg-transparent border-warning">
        <a href="NULL" className="btn btn-primary col">Profile</a>
      </div>
    </div>
  );
}

export default card;