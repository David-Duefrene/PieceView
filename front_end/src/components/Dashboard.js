import React from 'react';

import $ from "jquery";

import CardDeck from '../containers/CardDeck';


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
    $("#Followers").attr("class", "nav-item active");
  }

  /**
   * Renders the class.
   */
  render() {
    var listItems = this.state.tabs.map((item) =>
      <li key={item} id={item} className="nav-item col-4-md">
        <a className="nav-link" data-toggle="tab"
           href={"#" + item.toLowerCase()}>
          {item}
        </a>
      </li>
    )

    return (
      <div>
        <ul className="nav nav-tabs">{listItems}</ul>
        <div className="d-flex tab-content col-12">
          <div className="tab-pane active" id="followers">
            <CardDeck className='col' user_type="followers" />
          </div>
          <div className="tab-pane" id="following">
            <CardDeck user_type="following" />
          </div>
        </div>
      </div>
    );
  }
}

export default Dashboard;
