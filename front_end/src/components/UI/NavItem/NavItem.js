import React from 'react'
import PropTypes from 'prop-types';
import { NavLink, withRouter } from 'react-router-dom';

import CSS from './NavItem.module.css';


/**
 * Renders an individual navigation item for the navigation bar.
 * @param {string} props.path - The path to the page the link should go to.
 * @param {bool} props.exact - If the link should be a direct match.
 */
const navItem = props => {
    let isActive = CSS.NavItem;

    if (props.match.url === props.path) {
        isActive = CSS.NavItem  + ' ' + CSS.Active;
    }

    return (
        <li className={isActive}>
            <NavLink
                to={props.path}
                activeClassName={CSS.active}
                exact={props.exact} >
                {props.children}
            </NavLink>
        </li>
    );
};

navItem.propTypes = { path: PropTypes.string, exact: PropTypes.bool };

const NavItem = withRouter(navItem);

export const NavItemTest = navItem;

export default NavItem;
