import React from 'react';

import CSS from './PaginateButtons.module.css';

/**
 * Renders the buttons to cycle through the card deck.
 * @param {int} props.user_type - The user type to reference the buttons.
 * @param {func} props.first - The function to move to the first page.
 * @param {func} props.next - The function to move to the next page.
 * @param {func} props.prev - The function to move to the previous page.
 * @param {func} props.last - The function to move to the last page.
 */
const paginateButtons = props => {
    return (
        <div className={CSS.ButtonBox}>
            <ul className={CSS.ButtonList}>
                <li>
                    <button className={CSS.Button} onClick={props.first}>
                        &laquo; first
                    </button>
                </li>

                <li>
                    <button className={CSS.Button} onClick={props.prev}>
                        Previous page
                    </button>
                </li>

                <li>
                    <button className={CSS.PageNum}>Page
                        <span
                            className={"current-page-" + props.user_type}>
                            1
                        </span>
                        of TODO.
                    </button>
                </li>

                <li>
                    <button className={CSS.Button} onClick={props.next}>
                        Next Page
                    </button>
                </li>

                <li>
                    <button className={CSS.Button} onClick={props.last}>
                        last &raquo;
                    </button>
                </li>
            </ul>
        </div>
    );
}

export default paginateButtons;
