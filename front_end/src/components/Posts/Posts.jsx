import React, { Component } from 'react';
import PropTypes from 'prop-types';

import axios from '../../axios';
import axiosAuth from '../../axios-auth';
import PostStrip from './PostStrip/PostStrip';
import CSS from './Posts.module.css';

/**
 * Renders all posts currently posted.
 */
export class Posts extends Component {
    /**
     * Displays the posts currently active.
     * @extends Component
     * @param {string} type The type of posts the component is displaying
     * @param {string} title The title for posts the component is displaying
     * @param {bool} auth If the user needs to be authenticated
     * @prop {int} pageNum The current page number. Default is 1
     * @prop {list} postList The current active posts list
     * @prop {int} maxPage The maximum page number
     * @prop {bool} isLoaded States if we have loaded from the server
     * @prop {string} stateError The error string we may get from server
     * @prop {string} nextPage The url for the next page
     * @prop {string} prevPage The url for the previous page
     */
    state = {
        pageNum: 0,
        postList: [],
        maxPage: null,
        isLoaded: false,
        stateError: null,
        nextPage: null,
        prevPage: null,
    };

    /**
     * Loads first page of the active posts on the server
     */
    componentDidMount() {
        this.loadPosts();
        this.scrollListener = window.addEventListener('scroll', (e) => this.handleScroll(e));
    }

    /**
     * Loads the post based off of state.pageNum
     * @param {string} url - The url to load the posts from
     * @async
     */
    loadPosts = (url = 'post/api/postList/') => {
        const { type, auth } = this.props;
        const {
            postList, pageNum, maxPage, isLoaded,
        } = this.state;
        const data = {
            params: { type },
        };

        const newPage = pageNum + 1;
        if (newPage > maxPage && isLoaded) {
            return;
        }

        if (auth) {
            axiosAuth.get(url, data).then((result) => this.setState({
                maxPage: Math.ceil(result.data.count / 5),
                postList: [...postList, ...result.data.results],
                isLoaded: true,
                pageNum: newPage,
                nextPage: result.data.next,
                prevPage: result.data.previous,
            })).catch((error) => this.setState({ stateError: error }));
        } else {
            axios.get(url, data).then((result) => this.setState({
                maxPage: Math.ceil(result.data.count / 5),
                postList: [...postList, ...result.data.results],
                isLoaded: true,
                pageNum: newPage,
                nextPage: result.data.next,
                prevPage: result.data.previous,
            })).catch((error) => this.setState({ stateError: error }));
        }
    }

    /**
     * Handles the user scrolling
     */
    handleScroll = () => {
        const lastLi = document.querySelector(`div > div.${CSS.Posts}`);
        const lastLiOffset = lastLi.offsetTop + lastLi.clientHeight;
        const pageOffset = window.pageYOffset + window.innerHeight;

        if (pageOffset > lastLiOffset) {
            this.loadPosts();
        }
    };

    /**
     * Loads the previous page
     */
    previousClicked = () => {
        const { prevPage, pageNum } = this.state;
        if (prevPage !== null) {
            this.loadPosts(prevPage);
            this.setState({ pageNum: pageNum - 1 });
        }
    }

    /**
     * Loads the next page
     */
    nextClicked = () => {
        const { nextPage, pageNum } = this.state;
        if (nextPage !== null) {
            this.loadPosts(nextPage);
            this.setState({ pageNum: pageNum + 1 });
        }
    }

    /**
     * Loads the first page
     */
    firstClicked = () => {
        const { postList } = this.state;
        if (postList.first !== null) {
            this.loadPosts();
            this.setState({ pageNum: 1 });
        }
    }

    /**
     * Loads the last page
     */
    lastClicked = () => {
        const { postList, maxPage } = this.state;
        if (postList.last !== null) {
            this.loadPosts(`post/api/postList/?page=${maxPage}`);
            this.setState({ pageNum: maxPage });
        }
    }

    /**
     * Renders the component
     */
    render() {
        const { isLoaded, postList, stateError } = this.state;
        const { title } = this.props;

        if (!isLoaded) {
            return (<h1 className={CSS.Header}>Posts is loading.</h1>);
        }
        if (stateError != null) {
            return (<h1>{`Error: ${stateError}.`}</h1>);
        }

        const posts = [];

        for (let i = 0; i < postList.length; i++) {
            const postPK = postList[i].get_absolute_url.replace(/^\D+/g, '');
            posts.push(
                <PostStrip
                    title={postList[i].title}
                    body={postList[i].summary}
                    created={postList[i].created}
                    user={postList[i].authors}
                    key={i}
                    ID={postPK}
                />,
            );
        }

        return (
            <div className={CSS.Main}>
                <h1 className={CSS.Header}>{title}</h1>
                <div className={CSS.Posts}>{posts}</div>
            </div>
        );
    }
}

Posts.propTypes = {
    auth: PropTypes.bool,
    type: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
};

Posts.defaultProps = {
    auth: false,
};

export default Posts;
