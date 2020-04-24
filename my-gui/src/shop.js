import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'

function Shop() {
    useEffect(() => {
        fetchItems();
    },[]);

    const [items, setItems] = useState([]);

    const fetchItems = async () => {
        const data = await fetch("http://127.0.0.1:5000/users");

        const items = await data.json();
        console.log(items);
        setItems(items);
    };

    return (
        <div>
            <h1>Users List</h1>
            {items.map(item => (
                <h3 key={item.user_id}>{item.user_name}:
                    <Link to={`/shop/${item.user_id}`}> {item.user_id}</Link>
                </h3>
            ))}
        </div>
    );
}

export default Shop;
