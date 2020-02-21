import React from 'react';
import ReactDOM from 'react-dom';
import CardDeck from './CardDeck';

ReactDOM.render(
  <div>
    <CardDeck user_type="followers" />
    <CardDeck user_type="following" />
  </div>,
  document.getElementById('root')
);
