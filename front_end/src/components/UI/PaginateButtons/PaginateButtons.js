import React from 'react';

/**
 * Renders the buttons to cycle through the card deck.
 * @param {int} props.user_type - The user type to reference the buttons.
 * @param {func} props.first - The function to move to the first page.
 * @param {func} props.next - The function to move to the next page.
 * @param {func} props.prev - The function to move to the previous page.
 * @param {func} props.last - The function to move to the last page.
 */
function paginateButtons(props) {  
  return (
    <div className="d-flex deck-footer">
      <ul className="pagination">
        <li className="page-item">
          <button
            className={"page-link first-" + props.user_type}
            onClick={props.first}>
            &laquo; first
          </button>
        </li>

        <li className="page-item">
          <button
            className={"page-link previous-" + props.user_type}
            onClick={props.prev}>
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
          <button
            className={"page-link next-" + props.user_type}
            onClick={props.next}>
            Next Page
          </button>
        </li>

        <li className="page-item">
          <button
            className={"page-link last-" + props.user_type}
            onClick={props.last}>
            last &raquo;
          </button>
        </li>
      </ul>
    </div>
  );
}

export default paginateButtons;