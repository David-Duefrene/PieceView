/* eslint-disable no-restricted-syntax */
/* eslint-disable guard-for-in */
import React, { Component } from 'react';
import PropTypes from 'prop-types';

import CSS from './NavBoard.module.css';

/**
 * Renders a set of board navigated by tabs
 * @extends Component
 * @param {object} boards - An ordered dict of names and components for the boards
 *      @param {string} name - The name of the board
 *      @param {string} element - The element of the board
 * @prop {string} activeTab - The current active tab
 */
export class NavBoard extends Component {
    state = {
        // eslint-disable-next-line react/destructuring-assignment
        activeTab: this.props.boards[0].name,
    };

    /**
     * Changed the active tab.
     * @param {string} tabName - The tab to make active.
     */
    onTabClickedHandler = (tabName) => {
        this.setState({ activeTab: tabName });
    };

    /**
     * Renders the class
     */
    render() {
        const { activeTab } = this.state;
        const { boards } = this.props;
        const tabNames = [];
        let element = null;

        // Generate the tabs and find the active element
        boards.forEach((board) => {
            tabNames.push((
                <li key={board.name} id={board.name} className={CSS.NavItem}>
                    <button
                        type='button'
                        className={activeTab === board.name
                            ? CSS.Active.concat(' ', CSS.NavLink)
                            : CSS.NavLink}
                        onClick={() => this.onTabClickedHandler(board.name, board.element)}
                        id={board.name}
                    >
                        {board.name}
                    </button>
                </li>
            ));
            if (board.name === activeTab) {
                element = board.element;
            }
        });

        return (
            <div>
                <div className={CSS.TabBar}>{tabNames}</div>
                {element}
            </div>
        );
    }
}

NavBoard.propTypes = {
    boards: PropTypes.objectOf({
        name: PropTypes.string.isRequired,
        element: PropTypes.element.isRequired,
    }).isRequired,
};

export default NavBoard;
