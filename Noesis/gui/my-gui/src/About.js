import React from 'react';
import './App.css';
import brain from './icons/bci.jpg'
function About() {
    return (
        <div>
            <img className={"animated fadeIn color-image"}
            styles={{width: 400}}
            src={brain}/>
            <p>A website which visualizes cognition snapshots that were uploaded to the server,<br></br>
            where multiple parsers read the snapshots, parsed various parts of it, and publish the parsed results,<br></br>
            which are then saved to a database and you can view them on this website.</p>
        </div>
    );
}

export default About;
