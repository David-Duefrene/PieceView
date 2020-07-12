import React from 'react';
import PropTypes from 'prop-types';
import { NavLink, withRouter } from 'react-router-dom';

import CSS from './NavItem.module.css';

/**
 * Renders an individual navigation item for the navigation bar.
 * @param {string} props.path - The path to the page the link should go to.
 * @param {bool} props.exact - If the link should be a direct match.
 */
const navItem = (props) => {
    const {
        match, path, exact, children,
    } = props;
    let isActive = CSS.NavItem;

    if (match.url === path) {
        isActive = `${CSS.NavItem} ${CSS.Active}`;
    }

    return (
        <li className={isActive}>
            <NavLink to={path} activeClassName={CSS.active} exact={exact}>
                {children}
            </NavLink>
        </li>
    );
};

navItem.propTypes = {
    path: PropTypes.string.isRequired,
    match: PropTypes.string.isRequired,
    children: PropTypes.string.isRequired,
    exact: PropTypes.bool.isRequired,
};

const NavItem = withRouter(navItem);

export const NavItemTest = navItem;

export default NavItem;
