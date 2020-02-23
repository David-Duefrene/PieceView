import React from 'react';
import { Provider } from 'react-redux';

import CardDeck from './CardDeck';
import store from './store'


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
    <Provider store={store}>
      <div>
        <ul className="nav nav-tabs">{listItems}</ul>
        <div className="d-flex tab-content col-12">
          <div className="tab-pane active" id="followers">
            <CardDeck user_type="followers" />
          </div>
          <div className="tab-pane" id="following">
            <CardDeck user_type="following" />
          </div>
        </div>
      </div>
    </Provider>
    );
  }
}

export default Dashboard;
