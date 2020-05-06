import React from 'react';
import './App.css';
import Nav from './Nav'
import About from "./About";
import Users from "./users";
import User from "./user";
import Snapshots from "./snapshots";
import Snapshot from "./snapshot";
import Feelings from "./feelings"
import ColorImage from "./color_image"
import DepthImage from "./depth_image"
import Pose from "./pose"
import ColorImageData from "./color_image_data";


import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'

function App() {
  return (
      <Router>
          <div className="App">
              <Nav />
              <Switch>
              <Route path="/" exact component={Home}/>
              <Route path="/about" component={About}/>
              <Route path="/users" exact component={Users}/>
              <Route path="/users/:id" exact component={User}/>
              <Route path="/users/:id/snapshots" exact component={Snapshots}/>
              <Route path="/users/:id/snapshots/:snapshot" exact component={Snapshot}/>
              <Route path="/users/:id/snapshots/:snapshot/feelings" component={Feelings}/>
              <Route path="/users/:id/snapshots/:snapshot/depth_image" component={DepthImage}/>
              <Route path="/users/:id/snapshots/:snapshot/pose" component={Pose}/>
              <Route path="/users/:id/snapshots/:snapshot/color_image" exact component={ColorImage}/>
              <Route path="/users/:id/snapshots/:snapshot/color_image/data" component={ColorImageData}/>
              </Switch>
          </div>
      </Router>
  );
}

const Home = () => (
    <div>
        <Link className={"home-page"} to={`/users`}>Start</Link>
    </div>
);

export default App;
