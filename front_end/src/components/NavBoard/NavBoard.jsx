/* eslint-disable no-restricted-syntax */
/* eslint-disable guard-for-in */
import React, { Component } from 'react';
import PropTypes from 'prop-types';

import CSS from './NavBoard.module.css';

/**
 * Renders a set of board navigated by tabs
 * @extends Component
 * @param {object} boards - An ordered dict of names and components for the boards
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
        const elements = [];

        for (const i in boards) {
            tabNames.push(boards[i].name);
            elements.push(boards[i].element);
        }

        // Generate the tabs here
        const tabs = tabNames.map((name) => (
            <li key={name} id={name} className={CSS.NavItem}>
                <button
                    type='button'
                    className={activeTab === name
                        ? CSS.Active.concat(' ', CSS.NavLink)
                        : CSS.NavLink}
                    onClick={() => this.onTabClickedHandler(name)}
                    id={name}
                >
                    {name}
                </button>
            </li>
        ));

        return (
            <div>
                <div className={CSS.TabBar}>{tabs}</div>
                {elements}
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
