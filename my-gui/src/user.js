import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'

function User({ match }) {
    useEffect(() => {
        fetchItems();
        console.log(match);
    }, []);

    const [items, setItems] = useState({});
    const fetchItems = async () => {
        const fetchItem = await fetch(
            `http://127.0.0.1:5000/users/${match.params.id}`);
        const items = await fetchItem.json();

        console.log(items);
        setItems(items);
    };

    return (
        <div>

        </div>
    );
}

export default User;