import React from 'react';
import './App.css';
import { Link } from 'react-router-dom'
import home_button from './icons/home_icon.png'
import './styles/snapshots.scss';
import{ Component } from 'react';

class Nav extends Component {

    constructor(props) {
        super(props);
        this.state={}
    }

    async componentDidMount() {
    }

    render() {
        return (
            <nav>
                <a href='http://127.0.0.1:3000/'>
                <img
                    style={{ width: 30, height: 30}}
                    src={home_button}/>
                </a>
                    <ul className="nav-links">
                        <Link className="top_bar_links" to='/about'>
                            <li>About</li>
                        </Link>
                        <Link className="top_bar_links" to="/users">
                            <li>Users</li>
                        </Link>
                    </ul>
            </nav>
        )
    }
}

export default Nav;
