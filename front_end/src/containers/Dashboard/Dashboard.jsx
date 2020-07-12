import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import CardDeck from '../../components/CardDeck/CardDeck';
import UpdateProfile from './UpdateProfile/UpdateProfile';
import CSS from './Dashboard.module.css';

/**
 * Renders the Dashboard for a logged in user.
 * @property {arrayOfStrings} tabs - The tabs available on the Dashboard.
 * @property {string} activeTab - The current active tabs.
 */
export class Dashboard extends Component {
    state = {
        tabs: ['Profile', 'Followers', 'Following'],
        activeTab: 'Followers',
    };

    /**
     * Changed the active tab.
     * @param {string} tabName - The tab to make active.
     */
    onTabClickedHandler = (tabName) => {
        this.setState({ activeTab: tabName });
    };

    /**
     * Renders the class.
     */
    render() {
        const { tabs, activeTab } = this.state;
        const { user } = this.props;
        // Generate the tabs here
        const tabLinks = tabs.map((item) => (
            <li key={item} id={item} className={CSS.NavItem}>
                <button
                    type='button'
                    className={activeTab === item
                        ? CSS.Active.concat(' ', CSS.NavLink)
                        : CSS.NavLink}
                    onClick={() => this.onTabClickedHandler(item)}
                >
                    {item}
                </button>
            </li>
        ));

        // Generate content here
        let tabContent;
        switch (activeTab) {
        case 'Followers':
            tabContent = (
                <>
                    <h1>Followers clicked.</h1>
                    <CardDeck className='Followers' userType='followers' user={user} />
                </>
            );
            break;

        case 'Following':
            tabContent = (
                <>
                    <h1>Following Clicked.</h1>
                    <CardDeck className='Following' userType='following' user={user} />
                </>
            );
            break;

        case 'Profile':
            tabContent = (
                <>
                    <h1>Profile Clicked.</h1>
                    <UpdateProfile user={user} />
                </>
            );
            break;

        default:
            tabContent = (
                <>
                    <h1>Followers defaulted.</h1>
                    <CardDeck className='Followers' user_type='followers' user={user} />
                </>
            );
            break;
        }

        return (
            <div>
                <div className={CSS.TabBar}>
                    <ul className={CSS.NavTabs}>{tabLinks}</ul>
                </div>
                <div className={CSS.TabContent}>
                    {tabContent}
                </div>
            </div>
        );
    }
}

/**
 * @property {object} user - The current logged in user.
 */
const mapStateToProps = (state) => ({
    user: state.auth.user,
});

Dashboard.propTypes = {
    user: PropTypes.shape({
        first_name: PropTypes.string.isRequired,
        last_name: PropTypes.string.isRequired,
        photo: PropTypes.string.isRequired,
    }).isRequired,
};

export default connect(mapStateToProps)(Dashboard);
