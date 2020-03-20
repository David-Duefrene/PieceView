import React from 'react';

import $ from "jquery";

import CardDeck from '../CardDeck/CardDeck';
import CSS from './Dashboard.module.css';


class Dashboard extends React.Component {
  /**
   * Constructor
   * @param props.tabs - the names of the tabs for this instance.
   */
  constructor(props) {
    super(props);
    this.state = {
      tabs: props.tabs,
    };
  }

  /**
   * For once page is loaded, change Followers tab as active by default for now.
   */
  componentDidMount() {
    $("#Followers").attr("class", CSS.NavItem);
  }

  /**
   * Renders the class.
   */
  render() {
    var listItems = this.state.tabs.map((item) =>
      <li key={item} id={item} className={CSS.NavItem}>
        <a
          className={CSS.NavLink}
          data-toggle="tab"
          href={"#" + item.toLowerCase()}>
          {item}
        </a>
      </li>
    )

    return (
      <div>
        <ul className={CSS.NavTabs}>{listItems}</ul>
        <div className={CSS.TabContent}>
          <div className={CSS.TabPane} id="followers">
            <CardDeck className='' user_type="followers" />
          </div>
          <div className={CSS.TabPane} id="following">
            <CardDeck user_type="following" />
          </div>
        </div>
      </div>
    );
  }
}

export default Dashboard;
