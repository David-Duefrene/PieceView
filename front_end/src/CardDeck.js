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
 */
function Card(props) {
  return (
    <div className="card bg-transparent border-warning"
         id={"Follower"+props.number}>
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
 */
function PaginateButtons() {
  return (
    <ul className="pagination">
      <li className="page-item">
        <button className="page-link first">&laquo; first</button>
      </li>

      <li className="page-item">
        <button className="page-link previous">Previous page</button>
      </li>

      <li className="page-item disabled">
        <button className="page-link follower-page centered-link">
          Page <span className="follower-current-page">1</span> of TODO.
        </button>
      </li>

      <li className="page-item">
        <button className="page-link next">Next Page</button>
      </li>

      <li className="page-item">
        <button className="page-link last">last &raquo;</button>
      </li>
    </ul>
  );
}

/* Class  representing followers */
class UserCards extends React.Component {
  /**
   * Constructor
   */
  constructor(props) {
    super(props);
    this.state = {
      followers_list: [],
      isLoaded: false,
      page_limit: 4,
      page_num: 1,
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
        request_type: 'followers'
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
          followers_list: result.followers,
        });

        for (var i = 0; i < this.state.page_limit; i++) {
          $('#Follower'+i+' img.card-img-top').attr("src",
            this.state.followers_list[i]['photo']);
          $('#Follower'+i+' div.card-footer a.btn').attr("href",
            this.state.followers_list[i]['url']);
          $('#Follower'+i+' .card-body .card-title').text(
            this.state.followers_list[i]['name']);
        }

        $(".first").click(this.first);
        $(".previous").click(this.previous);
        $(".next").click(this.next);
        $(".last").click(this.last);
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
   * Changes teh cards to new set of users.
   * @param start - the index in the followers_list the loop should start at.
   */
  change(start) {
    for (var i = 0; i < this.state.page_limit; i++) {
      $('#Follower'+i+' img.card-img-top').attr("src",
        this.state.followers_list[i + start]['photo']);
      $('#Follower'+i+' div.card-footer a.btn').attr("href",
        this.state.followers_list[i + start]['url']);
      $('#Follower'+i+' .card-body .card-title').text(
        this.state.followers_list[i + start]['name']);
    }
  }

  /**
   * Gets the first set of cards in followers_list.
   */
  first() {
    this.change(0);
    this.setState({"page_num": 1});
  }

  /**
   * Gets the previous set of cards in followers_list.
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
   * Gets the next set of cards in followers_list.
   */
  next() {
    var new_page = this.state.page_num + 1;
    if (new_page * this.state.page_num >=
        this.state.followers_list.length) {
      this.last();
    }
    else {
      this.change(this.state.page_num * this.state.page_limit);
      this.setState({"page_num": new_page});
    }
  }

  /**
   * Gets the last set of cards in followers_list.
   */
  last() {
    var new_page = Math.ceil(this.state.followers_list.length /
                             this.state.page_limit);
    this.change(this.state.followers_list.length - this.state.page_limit);
    this.setState({"page_num": new_page});
  }

  /**
   * Renders the class.
   */
  render() {
    return (
      <div className="d-flex tab-content col-12">
        <div className="card-deck">
          <Card number="0"/>
          <Card number="1"/>
          <Card number="2"/>
          <Card number="3"/>
        </div>
        <div className="d-flex deck-footer">
          <PaginateButtons />
        </div>
      </div>
    );
  }
}

function CardDeck(props) {
  return (
    <div className="App">
      <UserCards />
    </div>
  );
}

export default CardDeck;
