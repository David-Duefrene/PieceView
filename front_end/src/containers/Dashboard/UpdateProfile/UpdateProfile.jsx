import React, { Component } from 'react';
import PropTypes from 'prop-types';

import CSS from './UpdateProfile.module.css';

/**
 * Form for a user to update their profile.
 * @prop {object} form The form the user will use
 * @prop {string} form.firstName Field for the user's first name. It is a text
 *  input and is optional.
 * @prop {string} form.lastName Field for the user's last name. It is a text
 *  input and is optional.
 * @prop {string} form.email Field for the user's email address. It is a text
 *  input and is a required field.
 * @prop {file} form.photo Field for the user's profile photo. It is a file
 *  input field and is optional.
 */
class UpdateProfile extends Component {
    state= {
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
            photo: {
                elementType: 'input',
                label: 'photo',
                dataType: 'file',
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
        this.setState({
            form: {
                firstName: { value: user.first_name },
                lastName: { value: user.last_name },
                email: { value: user.email },
                photo: { value: user.photo },
            },
        });
    }

    /**
     * Called when the user updates a field.
     * @param {object} input The input field itself.
     */
    onTextChangeHandler = (input) => {
        const { form } = this.state;
        form[input.target.name].value = input.target.value;
        this.setState({ form });
    }

    render() {
        const { user } = this.props;
        const { form } = this.state;
        let photo = null;
        const newForm = (
            Object.entries(form).map((element) => {
                if (element[0] === 'photo') {
                    photo = <img alt='' src={user.photo} />;
                }
                return (
                    <div
                        className={CSS.inputGroup}
                        key={element[0]}
                    >
                        {photo}
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
                );
            })
        );

        return (
            <form className={CSS.ProfileForm}>
                <h2>{`Welcome ${user.username}.`}</h2>
                <h2>You may edit your profile with the following form:</h2>
                {newForm}
            </form>
        );
    }
}

UpdateProfile.propTypes = {
    user: PropTypes.shape({
        username: PropTypes.string.isRequired,
        email: PropTypes.string.isRequired,
        first_name: PropTypes.string.isRequired,
        last_name: PropTypes.string.isRequired,
        photo: PropTypes.string.isRequired,
    }).isRequired,
};

export default UpdateProfile;
