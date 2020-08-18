import React from 'react';

import NavBoard from '../NavBoard/NavBoard';
import Posts from '../Posts/Posts';

/**
 * The home page, starts by rendering all posts
 */
const homePage = () => {
    const boards = {
        0: {
            name: 'All',
            element: (<Posts type='all' />),
        },
    };

    return (
        <NavBoard boards={boards} />
    );
};

export default homePage;
