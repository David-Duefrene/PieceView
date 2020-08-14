import React from 'react';
import PropTypes from 'prop-types';

import CSS from './PaginateButtons.module.css';

/**
 * Renders the buttons to cycle through the card deck.
 * @param {int} pageNum - The current page the user is on
 * @param {int} maxPages - The max number of pages available.
 * @param {func} first - The function to move to the first page
 * @param {func} next - The function to move to the next page
 * @param {func} prev - The function to move to the previous page
 * @param {func} last - The function to move to the last page
 */
const paginateButtons = (props) => {
    const {
        first, next, prev, last, pageNum, maxPages,
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
                        {`Page ${pageNum} of ${maxPages}`}
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
    pageNum: PropTypes.number.isRequired,
    maxPages: PropTypes.number.isRequired,
};

export default paginateButtons;
