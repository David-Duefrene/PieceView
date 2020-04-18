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
      },
      lastName: {
        elementType: 'input',
        label: 'Last Name',
        dataType: 'text',
        value: '',
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
      },
    });
  }

  onTextChangeHandler = (input) => {
    this.setState({ [input.target.name]: input.target.value })
  };

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
            <label className={CSS.formLabel}>{element['config']['label']}</label>
            <input
              type='text'
              name='fName'
              className={CSS.input}
              onChange={this.onTextChangeHandler}
              value={element['config']['value']} />
          </div>
      )})
    );

    return (
      <form className={CSS.ProfileForm} >
        <h2>Welcome {this.props.user.username}.</h2>
        <h2>You may edit your profile with the following form:</h2>
        {form}
      </form>
    );
  }
}

export default UpdateProfile;