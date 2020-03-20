import React from 'react';

/**
 * Renders the buttons to cycle through the card deck.
 * @param {int} props.user_type - The user type to reference the buttons.
 */
function paginateButtons(props) {
  return (
    <div className="d-flex deck-footer">
      <ul className="pagination">
        <li className="page-item">
          <button className={"page-link first-" + props.user_type}>
            &laquo; first
          </button>
        </li>

        <li className="page-item">
          <button className={"page-link previous-" + props.user_type}>
            Previous page
          </button>
        </li>

        <li className="page-item disabled">
          <button className="page-link follower-page centered-link">
            Page <span className={"current-page-" + props.user_type}>1</span> of
            TODO.
          </button>
        </li>

        <li className="page-item">
          <button className={"page-link next-" + props.user_type}>
            Next Page
          </button>
        </li>

        <li className="page-item">
          <button className={"page-link last-" + props.user_type}>
            last &raquo;
          </button>
        </li>
      </ul>
    </div>
  );
}

export default paginateButtons;