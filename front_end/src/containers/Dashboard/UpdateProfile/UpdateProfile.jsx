import React, { Component } from 'react';
import PropTypes from 'prop-types';

import { connect } from 'react-redux';

import Button from '../../../components/UI/Button/Button';
import { updateProfile } from '../../../store/actions/index';
import CSS from './UpdateProfile.module.css';

/**
 * Form for a user to update their profile.
 * @param {object} user The current logged in user
 * @prop {object} form The form the user will use
 * @prop {string} firstName Text input for the user's first name, it is optional.
 * @prop {string} lastName Text input for the user's last name, it is optional.
 * @prop {string} email Email input for the user's email address, it is required.
 * @prop {string} photo URL input for the user's profile photo, it is optional.
 */
export class UpdateProfile extends Component {
    state= {
        isLoaded: false,
        formMessage: null,
        form: {
            firstName: {
                elementType: 'input',
                label: 'First Name',
                dataType: 'text',
                value: '',
                id: 'firstName',
            },
            lastName: {
                elementType: 'input',
                label: 'Last Name',
                dataType: 'text',
                value: '',
                id: 'lastName',
            },
            email: {
                elementType: 'input',
                label: 'E-mail Address',
                dataType: 'email',
                value: '',
                id: 'email',
            },
            biography: {
                elementType: 'input',
                label: 'biography',
                dataType: 'textarea',
                value: '',
                id: 'photo',
            },
            photo: {
                elementType: 'input',
                label: 'photo',
                dataType: 'text',
                value: '',
                id: 'photo',
            },
        },
    };

    /**
     * Sets the state.
     */
    componentDidMount() {
        const { user } = this.props;
        const { form } = this.state;

        this.setState({
            isLoaded: true,
            form: {
                firstName: { ...form.firstName, value: user.first_name },
                lastName: { ...form.lastName, value: user.last_name },
                email: { ...form.email, value: user.email },
                photo: { ...form.photo, value: user.photo_url },
                biography: { ...form.biography, value: user.biography },
            },
        });
    }

    /**
     * Submits the form
     * @param {object} event
     */
    onSubmit = (event) => {
        event.preventDefault();
        const { form } = this.state;
        const { updateUser } = this.props;
        const data = {
            email: form.email.value,
            first_name: form.firstName.value,
            last_name: form.lastName.value,
            photo_link: form.photo.value,
            biography: form.biography.value,
        };
        this.setState({ isLoaded: false });
        updateUser(data);
    };

    /**
     * Called when the user updates a field.
     * @param {object} input The input field itself.
     */
    onTextChangeHandler = (input) => {
        const { form } = this.state;
        form[input.target.name].value = input.target.value;
        this.setState({ form });
    }

    /**
     * Renders the container
     */
    render() {
        const { user } = this.props;
        const { form, isLoaded, formMessage } = this.state;

        if (!isLoaded) {
            if (user !== null) {
                this.setState({ isLoaded: true });
            }
            return (<h1>Loading!!!</h1>);
        }
        const photo = (
            <img
                alt=''
                src={form.photo.value}
            />
        );

        const newForm = (
            Object.entries(form).map((element) => (
                <div className={CSS.inputGroup} key={element[0]}>
                    <label htmlFor={element[0]} className={CSS.formLabel}>
                        {element[1].label}
                    </label>
                    <input
                        type={element[1].dataType}
                        name={element[0]}
                        className={CSS.input}
                        onChange={this.onTextChangeHandler}
                        value={element[1].value}
                    />
                </div>
            ))
        );

        return (
            <form className={CSS.ProfileForm} onSubmit={this.onSubmit}>
                <h2>{`Welcome ${user.username}.`}</h2>
                <h2>You may edit your profile with the following form:</h2>
                {photo}
                {newForm}
                <Button type='submit'>Update Profile</Button>
                {formMessage === null ? '' : (<p>{formMessage}</p>)}
            </form>
        );
    }
}

const madDispatchToProps = (dispatch) => ({
    updateUser: (profile) => dispatch(updateProfile(profile)),
});

UpdateProfile.propTypes = {
    history: PropTypes.shape({ push: PropTypes.func.isRequired }).isRequired,
    updateUser: PropTypes.func.isRequired,
    user: PropTypes.shape({
        username: PropTypes.string.isRequired,
        email: PropTypes.string.isRequired,
        first_name: PropTypes.string.isRequired,
        last_name: PropTypes.string.isRequired,
        photo_url: PropTypes.string.isRequired,
        biography: PropTypes.string.isRequired,
    }).isRequired,
};

export default connect(() => {}, madDispatchToProps)(UpdateProfile);
