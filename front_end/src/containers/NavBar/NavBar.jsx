import React, { useReducer } from 'react';
import { useSelector } from 'react-redux';

import NavItem from '../../components/UI/NavItem/NavItem';
import LogoutButton from
    '../../components/UI/NavItem/LogoutButton/LogoutButton';
import * as actions from '../../store/actions/index';
import CSS from './NavBar.module.css';

/**
 * The navigation bar for the user to navigate the app.
 */
const NavBar = () => {
    const isAuth = useSelector((state) => state.auth.isAuthenticated);
    const [dispatch] = useReducer(actions.logout, { isAuth });

    return (
        <ul className={CSS.NavBar}>
            <NavItem path='/' exact>PieceView</NavItem>
            { isAuth ? (
                <>
                    <NavItem path='/dashboard'>Dashboard</NavItem>
                    <LogoutButton logoutReducer={dispatch}>
                        Logout
                    </LogoutButton>
                </>
            ) : (
                <>
                    <NavItem path='/register'>Register</NavItem>
                    <NavItem path='/login' exact={false}>Login</NavItem>
                </>
            )}
        </ul>
    );
};

export default NavBar;
