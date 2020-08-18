import React, { Component } from 'react';
import { withRouter } from 'react-router';
import PropTypes from 'prop-types';

import axios from '../../../axios';
import CSS from './Post.module.css';

/**
 * Renders and individual post amd comment section
 * @param {string} props.match.params.pk The primary key for the post
 */
export class Post extends Component {
    state = {
        isLoaded: false,
        title: '',
        content: '',
        author: '',
    };

    componentDidMount() {
        const { match } = this.props;
        axios.get(`post/api/post/${match.params.pk}`).then((result) => {
            this.setState({
                isLoaded: true,
                title: result.data.title,
                content: result.data.content,
                author: result.data.authors,
            });
        }).catch((error) => Error(error));
    }

    render() {
        const {
            isLoaded, title, content, author,
        } = this.state;

        return (
            <div>
                { isLoaded ? (
                    <div className={CSS.Post}>
                        <h1 className={CSS.Title}>{title}</h1>
                        <h3 className={CSS.Author}>{`${author.first_name} ${author.last_name}`}</h3>
                        <div
                            className={CSS.Content}
                            dangerouslySetInnerHTML={{ __html: content }}
                        />
                    </div>
                ) : (<h1>Loading!!!</h1>)}
            </div>
        );
    }
}

Post.propTypes = {
    match: PropTypes.shape({
        params: PropTypes.shape({
            pk: PropTypes.string.isRequired,
        }).isRequired,
    }).isRequired,
};

export default withRouter(Post);
