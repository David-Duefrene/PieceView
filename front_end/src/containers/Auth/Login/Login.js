import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import Button from '../../../components/UI/Button/Button'
import { login, loadUser } from '../../../store/actions/auth';
import store from '../../../store';
import CSS from './Login.module.css';

/**
 * Login form to authenticate a user.
 * @extends Component
 * @prop {object} form The form the user will fill out.
 * @prop {string} form.username The user's username.
 * @prop {string} form.password The user's password.
 * @prop {bool} isAuth If the user is authenticated.
 * @prop {func} login The function to log a user in.
 */
export class Login extends Component {
    state = {
        form: {
            username: {
                elementType: 'input',
                label: 'Username',
                dataType: 'text',
                value: '',
                id: 'username',
            },
            password: {
                elementType: 'input',
                label: 'Password',
                dataType: 'password',
                value: '',
                id: 'password',
            },
        },
        username: '',
        password: '',
        isAuth: false,
        login: PropTypes.func.isRequired,
    };

    /**
     * Loads user from local storage. If its not their it will set user to null.
     */
    componentDidMount() {
        store.dispatch(loadUser());
    }

    /**
     * Function for when the user submits the form.
     */
    onSubmit = event => {
        event.preventDefault();
        this.props.login(
            this.state.form.username.value,
            this.state.form.password.value
        );
    }

    /**
     * Function for when a user types into the form.
     */
    onChange = event => {
        let newForm = { ...this.state.form };
        newForm[event.target.name]['value'] = event.target.value;
        this.setState({ 'form': { ...newForm } });
    }

    /**
     * Function to render the form.
     * If the user is already authenticated form will redirect to homepage.
     */
    render() {
        if (this.props.isAuth) {
            return <Redirect to='/' />;
        }

        const form = this.state.form;
        const newForm = (Object.entries(this.state.form).map(element => {
            return(
                <div className={CSS.inputGroup} key={element[0]} >
                    <label className={CSS.label} > {element[1].label} </label>
                    <input
                        type={element[1].type}
                        className={CSS.input}
                        name={element[0]}

                        onChange={this.onChange}
                        value={element[1].value} />
                </div>
            )
        }))

        return (
            <form className={CSS.form} onSubmit={this.onSubmit}>
                <h2>Login</h2>
                {newForm}
                <div className={CSS.inputGroup}>
                    <Button type='submit' >
                        Login
                    </Button>
                </div>
                <p>
                    Don't have an account?
                    <Link to='/register'>Register</Link>
                </p>
            </form>
        );
    }
}

const mapStateToProps = state => ({
    isAuth: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { login })(Login);
