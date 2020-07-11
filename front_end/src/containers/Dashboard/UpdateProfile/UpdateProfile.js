import React, { Component } from 'react';

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
        this.setState({
            ...this.state,
            form: {
                ...this.state.form,
                firstName: {
                    ...this.state.form['firstName'],
                    value: this.props.user.first_name
                },
                lastName: {
                    ...this.state.form['lastName'],
                    value: this.props.user.last_name
                },
                email: {
                    ...this.state.form['email'],
                    value: this.props.user.email
                },
                photo: {
                    ...this.state.form['photo'],
                    value: this.props.user.photo
                },
            },
        });
    }

    /**
     * Called when the user updates a field.
     * @param {object} input The input field itself.
     */
    onTextChangeHandler = (input) => {
        let newForm = {...this.state.form};
        newForm[input.target.name]['value'] = input.target.value;
        this.setState({'form': {...newForm}});
    }

    render() {
        let photo = null;
        const form = (
            Object.entries(this.state.form).map(element => {
                if (element[0] == 'photo') {
                    photo = <img src={this.props.user.photo_url} />
                }
                return (
                    <div
                        className={CSS.inputGroup}
                        key={element[0]}>
                        {photo}
                        <label className={CSS.formLabel}>
                            {element[1]['label']}</label>
                        <input
                            type={element[1]['dataType']}
                            name={element[0]}
                            className={CSS.input}
                            onChange={this.onTextChangeHandler}
                            value={element[1]['value']} />
                    </div>
                );
            })
        );

        return (
            <form className={CSS.ProfileForm}>
                <h2>Welcome {this.props.user.username}.</h2>
                <h2>You may edit your profile with the following form:</h2>
                {form}
            </form>
        );
    }
}

export default UpdateProfile;
