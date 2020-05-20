import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';

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
        // Generate the tabs here
        const tabLinks = this.state.tabs.map((item) =>
            <li key={item} id={item} className={CSS.NavItem}>
            <button
                className={ this.state.activeTab === item ?
                CSS.Active.concat(' ', CSS.NavLink) :
                CSS.NavLink }
                onClick={() => this.onTabClickedHandler(item)} >
                {item}
            </button>
            </li>
        );

        // Generate content here
        let tabContent = undefined;
        switch(this.state.activeTab) {
            case 'Followers':
                tabContent = (
                    <Fragment>
                        <h1>Followers clicked.</h1>
                        <CardDeck
                            className='Followers'
                            user_type='followers'
                            user={this.props.user} />
                    </Fragment>
                );
                break;

            case 'Following':
                tabContent = (
                    <Fragment>
                        <h1>Following Clicked.</h1>
                        <CardDeck
                            className='Following'
                            user_type="following"
                            user={this.props.user} />
                    </Fragment>
                );
                break;

            case 'Profile':
                tabContent = (
                    <Fragment>
                        <h1>Profile Clicked.</h1>
                        <UpdateProfile user={this.props.user} />
                    </Fragment>
                );
                break;

            default:
                tabContent = (
                    <Fragment>
                        <h1>Followers defaulted.</h1>
                        <CardDeck
                            className='Followers'
                            user_type='followers'
                            user={this.props.user} />
                    </Fragment>
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
const mapStateToProps = state => {
    return {
        user: state.auth.user,
    };
};

export default connect(mapStateToProps)(Dashboard);
