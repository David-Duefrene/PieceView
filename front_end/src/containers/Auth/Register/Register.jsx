import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import Button from '../../../components/UI/Button/Button';
import CSS from '../Login/Login.module.css';
import { register, returnErrors } from '../../../store/actions/index';

/**
 * Register form to allow users to register.
 * @extends Component
 * @prop {object} form The form the user will fill out.
 * @prop {string} form.username The user's username.
 * @prop {string} form.email The user's email address.
 * @prop {string} form.password The user's password.
 * @prop {string} form.password2 The user's password for confirmation.
 * @prop {bool} isAuth If the user is authenticated.
 * @prop {action} register The action to register a user in.
 * @prop {action} returnErrors The action to execute if there are errors.
 */
export class Register extends Component {
    state = {
        form: {
            username: {
                elementType: 'input',
                label: 'Username',
                dataType: 'text',
                value: '',
                id: 'username',
            },
            email: {
                elementType: 'input',
                label: 'Email',
                dataType: 'email',
                value: '',
                id: 'email',
            },
            password: {
                elementType: 'input',
                label: 'Password',
                dataType: 'password',
                value: '',
                id: 'password',
            },
            password2: {
                elementType: 'input',
                label: 'Password2',
                dataType: 'password',
                value: '',
                id: 'password2',
            },
        },
    }

    onSubmit = (event) => {
        event.preventDefault();
        const { form } = this.state;
        const { returnErrorsFunc, registerFunc } = this.props;

        if (form.password.value !== form.password2.value) {
            returnErrorsFunc({ passwordNotMatch: 'Passwords do not match' });
        } else {
            const newUser = {
                username: form.username.value,
                password: form.password.value,
                email: form.email.value,
            };
            registerFunc(newUser);
        }
    };

    onChange = (event) => {
        const { form } = this.state;
        form[event.target.name].value = event.target.value;
        this.setState({ form });
    }

    render() {
        const { isAuthenticated } = this.props;
        const { form } = this.state;
        if (isAuthenticated) { return <Redirect to='/' />; }

        const renderedForm = (Object.entries(form).map((element) => (
            <div className={CSS.inputGroup} key={element[0]}>
                <label htmlFor={element[0]} className={CSS.label}>
                    {element[0]}
                </label>
                <input
                    type={element[1].dataType}
                    className={CSS.input}
                    name={element[0]}
                    onChange={this.onChange}
                    value={element[1].value}
                />
            </div>
        )));

        return (
            <form className={CSS.form} onSubmit={this.onSubmit}>
                <h2>Register</h2>
                {renderedForm}
                <div className={CSS.inputGroup}>
                    <Button type='submit'>
                        Register
                    </Button>
                </div>

                <p>
                    Already have an account?
                    {' '}
                    <Link to='/login'>Login</Link>
                </p>
            </form>
        );
    }
}

const mapStateToProps = (state) => ({
    isAuthenticated: state.auth.isAuthenticated,
});

Register.propTypes = {
    registerFunc: PropTypes.func.isRequired,
    returnErrorsFunc: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool.isRequired,
};

export default connect(mapStateToProps, { register, returnErrors })(Register);