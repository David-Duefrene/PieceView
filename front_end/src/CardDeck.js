import React from 'react';
import jQuery from "jquery";
import $ from "jquery";

/**
 * Obtains a cookie from the users browser.
 * @param {string} name - The name of the cookie needed.
 */
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

/**
 * Renders an individual card.
 * @param {int} props.number - The card ID number for the page.
 * @param {string} props.user_type - The user type for the cards.
 */
function Card(props) {
  return (
    <div className="card bg-transparent border-warning"
         id={props.user_type + props.number}>
      <img src="NULL" className="card-img-top img-responsive" />
      <div className="card-body">
        <h5 className="card-title">NULL</h5>
        <p className="card-text">Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Pellentesque dolor enim, facilisis a lectus ut,
        auctor efficitur est. Orci varius natoque penatibus et magnis dis
        parturient montes, nascetur ridiculus mus. Mauris et leo sapien.
        Etiam fringilla ultricies fringilla.</p>
      </div>
      <div className="card-footer bg-transparent border-warning">
        <a href="NULL" className="btn">Profile</a>
      </div>
    </div>
  );
}

/**
 * Renders the buttons to cycle through the card deck.
 * @param {int} props.user_type - The user type to reference the buttons.
 */
function PaginateButtons(props) {
  return (
    <ul className="pagination">
      <li className="page-item">
        <button className={"page-link first-" + props.user_type}>
          &laquo; first
        </button>
      </li>

      <li className="page-item">
        <button className={"page-link previous-" + props.user_type}>
          Previous page
        </button>
      </li>

      <li className="page-item disabled">
        <button className="page-link follower-page centered-link">
          Page <span className={"current-page-" + props.user_type}>1</span> of
          TODO.
        </button>
      </li>

      <li className="page-item">
        <button className={"page-link next-" + props.user_type}>
          Next Page
        </button>
      </li>

      <li className="page-item">
        <button className={"page-link last-" + props.user_type}>
          last &raquo;
        </button>
      </li>
    </ul>
  );
}

/* Class  representing followers */
class UserCards extends React.Component {
  /**
   * Constructor
   * @param props.user_type - The user type for this instance.
   */
  constructor(props) {
    super(props);
    this.state = {
      user_list: [],
      isLoaded: false,
      page_limit: 4,
      page_num: 1,
      user_type: props.user_type,
    };

    // Bind class methods here.
    this.first = this.first.bind(this);
    this.previous = this.previous.bind(this);
    this.next = this.next.bind(this);
    this.last = this.last.bind(this);
  }

  /**
   * Once page is loaded the function runs.
   */
  componentDidMount() {
    var data = JSON.stringify({
        page_limit: 500,
        page_num: 1,
        request_type: this.state.user_type
    });
    var csrftoken = getCookie('csrftoken');

    var payload = {
      method: 'POST',
      mode:'same-origin',
      body: data,
      headers: new Headers({
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        "X-CSRFToken": csrftoken}),
      credentials: 'include',
    };

    fetch("/account/ajax/users", payload).then(res => res.json()).then(
      (result) => {
        this.setState({
          isLoaded: true,
          user_list: result.followers,
        });

        this.change(0);

        // Bind button click events.
        $("button.first-" + this.state.user_type).click(this.first);
        $("button.previous-" + this.state.user_type).click(this.previous);
        $("button.next-" + this.state.user_type).click(this.next);
        $("button.last-" + this.state.user_type).click(this.last);
      },
      (error) => {
        console.log(error);
        this.setState({
          "isLoaded": true,
          error,
        });
      }
    )
  }

  /**
   * Changes the cards to new set of users.
   * @param start - the index in the user_list the loop should start at.
   */
  change(start) {
    for (var i = 0; i < this.state.page_limit; i++) {
      $('#' + this.state.user_type + i + ' img.card-img-top').attr("src",
        this.state.user_list[i + start]['photo']);
      $('#' + this.state.user_type + i + ' div.card-footer a.btn').attr("href",
        this.state.user_list[i + start]['url']);
      $('#' + this.state.user_type + i + ' .card-body .card-title').text(
        this.state.user_list[i + start]['name']);
    }
  }

  /**
   * Gets the first set of cards in user_list.
   */
  first() {
    this.change(0);
    this.setState({"page_num": 1});
  }

  /**
   * Gets the previous set of cards in user_list.
   */
  previous() {
    var new_page = this.state.page_num - 1;
    if (new_page < 1) { this.first(); }
    else {
      this.setState({"page_num": new_page});
      new_page -= 1;
      this.change(new_page * this.state.page_limit);
    }
  }

  /**
   * Gets the next set of cards in user_list.
   */
  next() {
    var new_page = this.state.page_num + 1;
    if (new_page * this.state.page_num >=
        this.state.user_list.length) {
      this.last();
    }
    else {
      this.change(this.state.page_num * this.state.page_limit);
      this.setState({"page_num": new_page});
    }
  }

  /**
   * Gets the last set of cards in user_list.
   */
  last() {
    var new_page = Math.ceil(this.state.user_list.length /
                             this.state.page_limit);
    this.change(this.state.user_list.length - this.state.page_limit);
    this.setState({"page_num": new_page});
  }

  /**
   * Renders the class.
   */
  render() {
    var cards = []

    for (var i = 0; i < 4; i++) {
      cards.push(<Card number={i} user_type={this.state.user_type} key={i} />)
    }

    return (
      <div className="d-flex tab-content col-12">
        <div className={"card-deck " + this.state.user_type}>
          {cards}
        </div>
        <div className="d-flex deck-footer">
          <PaginateButtons user_type={this.state.user_type} />
        </div>
      </div>
    );
  }
}

  /**
  * Card Deck itself.
  * @param props.user_type - type of user to display.
  */
function CardDeck(props) {
  return (
    <div className="App">
      <UserCards user_type={props.user_type}/>
    </div>
  );
}

export default CardDeck;
