import React from 'react';
import './App.css';
import { Link } from 'react-router-dom'
function Nav() {

    const navStyle = {
        color: '#F0E2C8'
    };

    return (
        <nav>
            <h3>Logo</h3>
            <ul className="nav-links">
                <Link style={navStyle} to='/about'>
                    <li>About</li>
                </Link>
                <Link style={navStyle} to="/users">
                    <li>Users</li>
                </Link>
            </ul>
        </nav>
    );
}

export default Nav;
