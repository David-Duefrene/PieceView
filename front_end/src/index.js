import ReactDOM from 'react-dom';
import Dashboard from './Dashboard';

ReactDOM.render(
  <Dashboard tabs={["Followers", "Following"]}/>,
  document.getElementById('root')
);
