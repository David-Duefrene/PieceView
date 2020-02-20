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

function PaginateButtons() {
  return (
    <ul className="pagination">
      <li className="page-item">
        <button className="page-link followers first">
          &laquo; first
        </button>
      </li>

      <li className="page-item">
        <button className="page-link followers previous">
          Previous page
        </button>
      </li>

      <li className="page-item disabled">
        <button className="page-link follower-page centered-link"
          data-limit="3">
          Page <span className="follower-current-page">1</span> of TODO.
        </button>
      </li>

      <li className="page-item">
        <button className="page-link followers next">
          Next Page
        </button>
      </li>

      <li className="page-item">
        <button className="page-link followers" data-action="last">
          last &raquo;
        </button>
      </li>
    </ul>
  )
}

class Followers extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      followers_list: [],
      isLoaded: false,
      total_cards: 0,
      card_deck: null,
      page_num: 1,
    };
    this.first = this.first.bind(this);
    this.previous = this.previous.bind(this);
    this.next = this.next.bind(this);
  }

  componentDidMount() {
    var data = JSON.stringify({
        page_limit: 500,
        page_num: 1,
        action: 'first',
        request_type: 'followers'
    });
    var csrftoken = getCookie('csrftoken');

    const payload = {
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
          card_deck: result,
        });
        console.log(this.state.card_deck);
        console.log(this.state.followers_list);

        for (var i = 0; i < 5; i++) {
          $(".card-deck").append(this.Card(i));
          $('#Follower'+i+' img.card-img-top').attr("src",
            this.state.followers_list[i]['photo']);
          $('#Follower'+i+' div.card-footer a.btn').attr("href",
            this.state.followers_list[i]['url']);
          $('#Follower'+i+' .card-body .card-title').text(
            this.state.followers_list[i]['name']);
        }
        // this.change(5);

        $(".first").click(this.first);
        $(".previous").click(this.previous);
        $(".next").click(this.next);

      },
      (error) => {
        console.log(error);
        this.setState({
          isLoaded: true,
          error
        });
      }
    )
  }

  change(start) {
    console.log("start: "+start);
    console.log(`length of deck: ${this.state.card_deck.length}`);
    for (var i = 0; i < 5; i++) {
      console.log(`i: ${i}`);
      $('#Follower'+i+' img.card-img-top').attr("src",
        this.state.card_deck['followers'][i + start]['photo']);
      $('#Follower'+i+' div.card-footer a.btn').attr("href",
        this.state.card_deck['followers'][i + start]['url']);
      $('#Follower'+i+' .card-body .card-title').text(
        this.state.card_deck['followers'][i + start]['name']);
    }
  }

  Card(number) {
      // Renders an individual card.
      var one =`<div className="card bg-transparent border-warning"
                     style="max-width: min-content; border: 1px solid #ffc107;"" id="Follower${number}">
                <img src="`
      var two = this.state.followers_list[number]['photo'] +
        `" className="card-img-top img-responsive" />
          <div className="card-body">
            <h5 className="card-title">`
      var three = this.state.followers_list[number]['name']+`</h5>
            <p className="card-text">Lorem ipsum dolor sit amet, consectetur
            adipiscing elit. Pellentesque dolor enim, facilisis a lectus ut,
            auctor efficitur est. Orci varius natoque penatibus et magnis dis
            parturient montes, nascetur ridiculus mus. Mauris et leo sapien.
            Etiam fringilla ultricies fringilla.</p>
          </div>

          <div className="card-footer bg-transparent border-warning" style=" border-top: 1px solid #ffc107">
            <a href="`
      var four = this.state.followers_list[number]['url']+`"
      className="btn" style="color: #fff; background-color: #007bff;
      border-color: #007bff; display: inline-block; font-weight: 400;
      padding: .375rem 6.75rem; font-size: 1rem; line-height: 1.5;
      border-radius: .25rem;">
      Profile</a>
          </div>
        </div>`
      return one+two+three+four;
    }

  first() {
    console.log("first method");
    this.change(0);
    this.setState({"page_num": 1})
  }

  previous() {
    console.log("previous method");
    if (this.state.page_num < 2) {
      console.log(`Trying to go to a negative page, redirected to first.`);
      this.first();
    }
    else {
      this.setState({"page_num": this.state.page_num - 1})
      console.log(`new page number: ${this.state.page_num}`);
      this.change(this.state.page_num*5)
    }
  }

  next() {
    console.log("next method");
    if (this.state.page_num > this.state.followers_list.length / 5 + 1) {
      console.log(`requesting more page than you have. redirected to last`);
    }
    else {
      this.change(this.state.page_num*5)
      this.setState({"page_num": this.state.page_num + 1})
      console.log(`new page number: ${this.state.page_num}`);
    }
  }

  render() {
    return (
      <div className="d-flex tab-content col-12">
        <div className="card-deck">

        </div>
        <div className="d-flex deck-footer">
          <PaginateButtons />
        </div>
      </div>
    );
  }
}

ReactDOM.render(
  <Followers />,
  document.getElementById('root')
);
