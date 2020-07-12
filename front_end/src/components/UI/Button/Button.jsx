/* eslint-disable react/button-has-type */
import React from 'react';
import PropTypes from 'prop-types';

import CSS from './Button.module.css';

/**
 * A UI button component for the app.
 * @param {string} type Specifies the button type.
 */
const button = (props) => {
    const { type, children } = props;
    return (
        <>
            <button className={CSS.Button} type={type}>
                {children}
            </button>
        </>
    );
};

button.propTypes = {
    type: PropTypes.string,
    children: PropTypes.string,
};

button.defaultProps = {
    type: 'submit',
    children: 'Button',
};

export default button;
