import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import Button from '../../../components/UI/Button/Button';
import { login } from '../../../store/actions/index';
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
    };

    /**
     * Function for when the user submits the form.
     */
    onSubmit = (event) => {
        event.preventDefault();
        const { onLogin } = this.props;
        const { form } = this.state;
        onLogin(form.username.value, form.password.value);
    }

    /**
     * Function for when a user types into the form.
     */
    onChange = (event) => {
        const { form } = this.state;
        form[event.target.name].value = event.target.value;
        this.setState({ form });
    }

    /**
     * Function to render the form.
     * If the user is already authenticated form will redirect to homepage.
     */
    render() {
        const { isAuth, messages } = this.props;
        const { form } = this.state;

        if (isAuth) { return <Redirect to='/' />; }

        const newForm = (Object.entries(form).map((element) => (
            <div className={CSS.inputGroup} key={element[0]}>
                <label htmlFor={element[1].label} className={CSS.label}>
                    {element[1].label}
                </label>
                <input
                    type={element[1].dataType}
                    className={CSS.input}
                    name={element[0]}
                    onChange={this.onChange}
                    value={element[1].value}
                    required
                />
                {
                    messages.message !== undefined
                        ? (<h5 className={CSS.error}>{messages.message.msg[element[0]]}</h5>)
                        : null
                }
            </div>
        )));

        return (
            <form className={CSS.form} onSubmit={this.onSubmit}>
                <h2>Login</h2>
                {messages.message !== undefined ? Object.entries(messages.message.msg)
                    .map((error) => (<h3 key={error[1]} className={CSS.error}>{error[1]}</h3>))
                    : null }
                {newForm}
                <div className={CSS.inputGroup}>
                    <Button type='submit'>
                        Login
                    </Button>
                </div>
                <p>
                    {'Don\'t have an account?'}
                    <Link to='/register'>Register</Link>
                </p>
            </form>
        );
    }
}

const mapStateToProps = (state) => ({
    isAuth: state.auth.isAuthenticated,
    messages: state.messages,
});

const madDispatchToProps = (dispatch) => ({
    onLogin: (username, password) => dispatch(login(username, password)),
});

Login.propTypes = {
    isAuth: PropTypes.bool.isRequired,
    messages: PropTypes.shape,
    onLogin: PropTypes.func.isRequired,
};

Login.defaultProps = {
    messages: {},
};

export default connect(mapStateToProps, madDispatchToProps)(Login);
