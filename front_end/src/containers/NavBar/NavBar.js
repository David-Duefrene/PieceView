import React, { Component } from 'react';
import { connect } from 'react-redux';

import NavItem from '../../components/UI/NavItem/NavItem';
import LogoutButton from
    '../../components/UI/NavItem/LogoutButton/LogoutButton' ;
import * as actions from '../../store/actions/index';
import CSS from './NavBar.module.css';


/**
 * The navigation bar for the user to navigate the app.
 */
export class NavBar extends Component {
    render() {
        return (
            <ul className={CSS.NavBar}>
                <NavItem path='/' exact>PieceView</NavItem>
                { this.props.isAuth?
                    <LogoutButton logoutReducer={this.props.onLogout}>
                        Logout</LogoutButton>:
                    <NavItem path='/login' exact={false}>Login</NavItem>
                }
            </ul>
        );
    };
};

/**
 * @prop {bool} isAuth If the user is authenticated.
 */
const mapStateToProps = state => {
    return { isAuth: state.auth.isAuthenticated };
};

/**
 * @prop {func} onLogout Function to logout the user.
 */
const madDispatchToProps = dispatch => {
    return { onLogout: ()=> dispatch(actions.logout()) };
};

export default connect(mapStateToProps, madDispatchToProps)(NavBar);
