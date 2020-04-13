import React from 'react'
import {NavLink, withRouter} from 'react-router-dom';

import CSS from './NavItem.module.css';


const navItem = (props) => {
  let isActive = CSS.NavItem;
  if (props.match.url === props.path) {
    isActive = CSS.NavItem  + ' ' + CSS.Active;
  }

  return (
  <li className={isActive}>
    <NavLink to={props.path} activeClassName={CSS.active} exact={props.exact}>
      {props.children}</NavLink>
  </li>
);}

const NavItem = withRouter(navItem);

export const NavItemTest = navItem;

export default NavItem;