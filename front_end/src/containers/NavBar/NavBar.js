import React, { Component } from 'react';
import { connect } from 'react-redux';

import NavItem from '../../components/UI/NavItem/NavItem';
import LogoutButton from
    '../../components/UI/NavItem/LogoutButton/LogoutButton' ;
import * as actions from '../../store/actions/index';
import CSS from './NavBar.module.css';


export class NavBar extends Component {
    static defaultProps = { onLogout: null };

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

const mapStateToProps = state => {
    return { isAuth: state.auth.isAuthenticated };
};

const madDispatchToProps = dispatch => {
    return { onLogout: ()=> dispatch(actions.logout()) };
};

export default connect(mapStateToProps, madDispatchToProps)(NavBar);
