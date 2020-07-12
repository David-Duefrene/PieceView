import React from 'react';
import PropTypes from 'prop-types';
import CSS from './PaginateButtons.module.css';

/**
 * Renders the buttons to cycle through the card deck.
 * @param {int} props.user_type - The user type to reference the buttons.
 * @param {func} props.first - The function to move to the first page.
 * @param {func} props.next - The function to move to the next page.
 * @param {func} props.prev - The function to move to the previous page.
 * @param {func} props.last - The function to move to the last page.
 */
const paginateButtons = (props) => {
    const {
        first, next, prev, last, userType,
    } = props;

    return (
        <div className={CSS.ButtonBox}>
            <ul className={CSS.ButtonList}>
                <li>
                    <button type='button' className={CSS.Button} onClick={first}>
                        &laquo; first
                    </button>
                </li>

                <li>
                    <button type='button' className={CSS.Button} onClick={prev}>
                        Previous page
                    </button>
                </li>

                <li>
                    <button type='button' className={CSS.PageNum}>
                        Page
                        <span className={`current-page-${userType}`}>
                            1
                        </span>
                        of TODO.
                    </button>
                </li>

                <li>
                    <button type='button' className={CSS.Button} onClick={next}>
                        Next Page
                    </button>
                </li>

                <li>
                    <button type='button' className={CSS.Button} onClick={last}>
                        last &raquo;
                    </button>
                </li>
            </ul>
        </div>
    );
};

paginateButtons.propTypes = {
    first: PropTypes.func.isRequired,
    next: PropTypes.func.isRequired,
    prev: PropTypes.func.isRequired,
    last: PropTypes.func.isRequired,
    userType: PropTypes.string.isRequired,

};

export default paginateButtons;
