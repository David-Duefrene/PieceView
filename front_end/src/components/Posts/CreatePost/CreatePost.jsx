import React, { Component } from 'react';

import RichTextEditor from 'react-rte';

import PropTypes from 'prop-types';

import Button from '../../UI/Button/Button';
import axiosAuth from '../../../axios-auth';
import CSS from './CreatePost.module.css';

/**
 * Allows a authenticated user to create a post
 * @extends Component
 * @prop {string} title The title for the user's post
 * @prop {RichText} content The content for a post, uses react-rte rich text format use toString
 *      ('html') to convert to html
 * @param {object} history the DOM history, allows us to redirect the user to their new post
 */
export class CreatePost extends Component {
    state = {
        title: null,
        content: RichTextEditor.createEmptyValue(),
    }

    /**
     * Submits the post to the server
     * @param {object} event The on submit event for the form
     */
    onSubmit = (event) => {
        event.preventDefault();
        const { title, content } = this.state;
        const { history } = this.props;
        const data = {
            title,
            content: content.toString('html'),
        };

        axiosAuth.post('post/api/postList/', data).then((result) => {
            history.push(result.data.URL);
        }).catch((error) => {
            throw new Error(error.toString());
        });
    };

    /**
     * Renders the component
     */
    render() {
        const { content, title } = this.state;
        return (
            <form className={CSS.Form} onSubmit={this.onSubmit}>
                <h1 className={CSS.Header}>Create a post.</h1>
                {/* eslint-disable-next-line jsx-a11y/label-has-associated-control */}
                <label className={CSS.Label} htmlFor='Title'>Title:</label>
                <input
                    type='text'
                    name='Title'
                    id='Title'
                    className={CSS.Input}
                    value={title}
                    onChange={(val) => this.setState({ title: val.target.value })}
                />
                <h3 className={CSS.Label}>Post Content</h3>
                <RichTextEditor
                    value={content}
                    className={CSS.Editor}
                    onChange={(val) => this.setState({ content: val })}
                />
                <Button className={CSS.Button} type='submit'>Submit Post</Button>
            </form>
        );
    }
}

CreatePost.propTypes = {
    history: PropTypes.shape({
        push: PropTypes.func.isRequired,
    }).isRequired,
};

export default CreatePost;
