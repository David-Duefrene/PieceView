import React from 'react';

import CardDeck from '../../containers/CardDeck/CardDeck';
import CSS from './Dashboard.module.css';


class Dashboard extends React.Component {
  state = {
    tabs: ['Followers', 'Following'],
    activeTab: 'Followers',
  };

   onTabClickedHandler = (tabName) => {
    this.setState({activeTab: tabName});
  };

  /**
   * Renders the class.
   */
  render() {
    const tabLinks = this.state.tabs.map((item) =>
      <li key={item} id={item} className={CSS.NavItem}>
        <button
          className={this.state.activeTab === item ? CSS.Active + ' ' + CSS.NavLink : CSS.NavLink}
          onClick={() => this.onTabClickedHandler(item)} >
          {item}
        </button>
      </li>
    )

    let currentDeck =(
      <React.Fragment>
        <h1>Followers initial.</h1>
        <CardDeck className='Followers' user_type='followers' />
      </React.Fragment>
    );
    switch(this.state.activeTab){
      case 'Followers':
        currentDeck =(
          <React.Fragment>
            <h1>Followers clicked.</h1>
            <CardDeck className='Followers' user_type='followers' />
          </React.Fragment>
        );
        break;
      case 'Following':
        currentDeck = (
          <React.Fragment>
            <h1>Following Clicked.</h1>
            <CardDeck className='Following' user_type="following" />
          </React.Fragment>
        );
        break;
      default:
        currentDeck =(
          <React.Fragment>
            <h1>Followers defaulted.</h1>
            <CardDeck className='Followers' user_type='followers' />
          </React.Fragment>
        );
        break;
    }

    return (
      <div>
        <div className={CSS.TabBar}>
          <ul className={CSS.NavTabs}>{tabLinks}</ul>
        </div>
        <div className={CSS.TabContent}>
          {currentDeck}
        </div>
      </div>
    );
  }
}

export default Dashboard;
