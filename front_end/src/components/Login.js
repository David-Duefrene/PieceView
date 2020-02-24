import React from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";

import { login, loadUser } from "../actions/auth";
import store from '../store'

export class Login extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      username: "",
      password: "",
      isAuthenticated: false,
      login: PropTypes.func.isRequired
    };

    this.onSubmit = this.onSubmit.bind(this);
    this.onChange = this.onChange.bind(this);
  }

  componentDidMount() {
    store.dispatch(loadUser());
  }

  onSubmit(e) {
    e.preventDefault();
    this.props.login(this.state.username, this.state.password);
  }

  onChange(e) {
    console.log(e);
    this.setState({ [e.target.name]: e.target.value });
  }

  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }

    const { username, password } = this.state;

    return (
      <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <h2 className="text-center">Login</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Username</label>
              <input type="text" className="form-control" name="username"
                     onChange={this.onChange} value={username}/>
            </div>

            <div className="form-group">
              <label>Password</label>
              <input type="password" className="form-control" name="password"
                     onChange={this.onChange} value={password}/>
            </div>

            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Login
              </button>
            </div>
            <p>
              Don't have an account? <Link to="/register">Register</Link>
            </p>
          </form>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { login })(Login);
