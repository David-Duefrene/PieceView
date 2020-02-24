import React from 'react';

import Dashboard from '../Dashboard';


class App extends React.Component {
  render() {
    return (
      <Dashboard tabs={['Followers', 'Following']} />
    );
  }
}

export default App;
