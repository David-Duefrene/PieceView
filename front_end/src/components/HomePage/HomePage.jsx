import React from 'react';

import { useSelector } from 'react-redux';

import NavBoard from '../NavBoard/NavBoard';
import Posts from '../Posts/Posts';

/**
 * The home page, starts by rendering all posts
 * If the user is authenticated is will also give the options to view the users followers posts
 */
const HomePage = () => {
    const isAuth = useSelector((state) => state.auth.isAuthenticated);

    const boards = [
        {
            name: 'All',
            element: <Posts key={0} title='All Posts' type='all' />,
        },

    ];

    if (isAuth) {
        boards.push({
            name: 'Followed Authors',
            element: <Posts auth key={1} title='Posts by people you follow' type='following' />,
        });
    }

    return (
        <NavBoard boards={boards} />
    );
};

export default HomePage;
