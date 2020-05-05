import React, { Component } from 'react';

import CSS from './UpdateProfile.module.css';


class UpdateProfile extends Component {
    state= {
        form: {
            firstName: {
                elementType: 'input',
                label: 'First Name',
                dataType: 'text',
                value: '',
                name: 'firstName',
            },
            lastName: {
                elementType: 'input',
                label: 'Last Name',
                dataType: 'text',
                value: '',
                name: 'lastName',
            },
            email: {
                elementType: 'input',
                label: 'E-mail Address',
                dataType: 'email',
                value: '',
                name: 'email',
            },
            photo: {
                elementType: 'input',
                label: 'photo',
                dataType: 'file',
                value: '',
                name: 'photo',
            },
        },
    };

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

    onTextChangeHandler = (input) => {
        let newForm = {...this.state.form}
        newForm[input.target.name]['value'] = input.target.value

        this.setState({'form': {...newForm}});
    }

    render() {
        const formElementsArray = [];
        for (const key in this.state.form) {
            formElementsArray.push({
                id: key,
                config: this.state.form[key],
            });
        }


        const form = (
            formElementsArray.map(element => {
                return (
                    <div className={CSS.inputGroup}>
                    <label className={CSS.formLabel}>
                        {element['config']['label']}</label>
                    <input
                        type={element['config']['dataType']}
                        name={element['config']['name']}
                        className={CSS.input}
                        onChange={this.onTextChangeHandler}
                        value={element['config']['value']} />
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