import React, { Component } from 'react';

import axios from '../../axios';
import PostStrip from './PostStrip/PostStrip';
import PaginateButtons from '../UI/PaginateButtons/PaginateButtons';
import CSS from './Posts.module.css';

/**
 * Renders all posts currently posted.
 */
export class Posts extends Component {
    /**
     * Displays the posts currently active.
     * @extends Component
     * @prop {int} pageNum The current page number. Default is 1
     * @prop {list} postList The current active posts list
     * @prop {int} maxPage The maximum page number
     * @prop {bool} isLoaded States if we have loaded from the server
     * @prop {string} stateError The error string we may get from server
     * @prop {string} nextPage The url for the next page
     * @prop {string} prevPage The url for the previous page
     */
    state = {
        pageNum: 1,
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
    }

    /**
     * Loads the post based off of state.pageNum
     * @param {string} url - The url to load the posts from
     * @async
     */
    loadPosts = (url = 'post/api/postList/') => {
        axios.get(url).then((result) => this.setState({
            maxPage: Math.ceil(result.data.count / 5),
            postList: result.data.results,
            isLoaded: true,
            nextPage: result.data.next,
            prevPage: result.data.previous,
        })).catch((error) => this.setState({ stateError: error }));
    }

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
        const {
            isLoaded, postList, stateError, pageNum, maxPage,
        } = this.state;

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
                    body={postList[i].content}
                    created={postList[i].created}
                    user={postList[i].authors}
                    key={i}
                    ID={postPK}
                />,
            );
        }

        return (
            <div className={CSS.Posts}>
                <h1 className={CSS.Header}>Posts</h1>
                {posts}
                <PaginateButtons
                    pageNum={pageNum}
                    maxPages={maxPage}
                    userType='posts'
                    first={this.firstClicked}
                    prev={this.previousClicked}
                    next={this.nextClicked}
                    last={this.lastClicked}
                />
            </div>
        );
    }
}

export default Posts;
