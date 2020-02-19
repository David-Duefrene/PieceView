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

class Followers extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      followers_list: [],
      isLoaded: false};
  }

  componentDidMount() {
    var data = JSON.stringify({
        page_limit: 1,
        page_num: 1,
        action: 'first',
        request_type: 'followers'
      })
      var csrftoken = getCookie('csrftoken');

    const res = {
       method: 'POST',
       mode:'no-cors',
       body: JSON.stringify(data),
       headers: new Headers({"X-CSRFToken": csrftoken}),
     };

    fetch("/account/ajax/users").then(res => res.json()).then(
      (result) => {
        console.log(result);
        this.setState({
          isLoaded: true,
          followers_list: result.followers
        });
        $('#Follower div.card-footer a.btn').attr("href",
          result['followers'][0]['url']);
        $('#Follower .card-body .card-title').text(
          result['followers'][0]['name']);
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

  render() {
    return (
      <div id="Follower">
        <div className="card-body">
          <h5 className="card-title">NULL</h5>
          <p className="card-text">Some default card text here</p>
        </div>

        <div className="card-footer">
          <a href="NULL" className="btn">Profile</a>
        </div>
      </div>
    );
  }
}

ReactDOM.render(
  <Followers />,
  document.getElementById('root')
);
