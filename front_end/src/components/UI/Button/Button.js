import React, { Fragment } from 'react';

import CSS from './Button.module.css'


/**
 * A UI button component for the app.
 * @param {string} type Specifies the button type.
 */
const button = props => {
    return (
        <Fragment>
            <button className={CSS.Button} type={props.type} >
                {props.children}
            </button>
        </Fragment>
    )
};

button.defaultProps = {
    type: 'submit',
};

export default button;
