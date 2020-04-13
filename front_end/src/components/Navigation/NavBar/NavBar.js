import React, {Component} from 'react';
import {connect} from 'react-redux';
// import {Route, NavLink} from 'react-router-dom';

import NavItem from './NavItem/NavItem';
import CSS from './NavBar.module.css';

export class NavBar extends Component{
   render() {
    return (
      <ul className={CSS.NavBar}>
        <NavItem path='/' exact>PieceView</NavItem>
        { this.props.isAuth? (<NavItem path='/logout'>Logout</NavItem>):
          <NavItem path='/login' exact={false}>Login</NavItem> }
      </ul>
    );
  }
}

const mapStateToProps = state => {
  return{
    isAuth: state.auth.isAuthenticated,
  };
};

export default connect(mapStateToProps)(NavBar);