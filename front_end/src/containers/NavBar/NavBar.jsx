import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import NavItem from '../../components/UI/NavItem/NavItem';
import LogoutButton from
    '../../components/UI/NavItem/LogoutButton/LogoutButton';
import * as actions from '../../store/actions/index';
import CSS from './NavBar.module.css';

/**
 * The navigation bar for the user to navigate the app.
 */
const navBar = (props) => {
    const { onLogout, isAuth } = props;
    return (
        <ul className={CSS.NavBar}>
            <NavItem path='/' exact>PieceView</NavItem>
            { isAuth
                ? (
                    <LogoutButton logoutReducer={onLogout}>
                        Logout
                    </LogoutButton>
                )
                : <NavItem path='/login' exact={false}>Login</NavItem>}
        </ul>
    );
};

/**
 * @prop {bool} isAuth If the user is authenticated.
 */
const mapStateToProps = (state) => ({ isAuth: state.auth.isAuthenticated });

/**
 * @prop {func} onLogout Function to logout the user.
 */
const madDispatchToProps = (dispatch) => ({ onLogout: () => dispatch(actions.logout()) });

navBar.propTypes = {
    isAuth: PropTypes.bool.isRequired,
    onLogout: PropTypes.func.isRequired,
};

export default connect(mapStateToProps, madDispatchToProps)(navBar);
