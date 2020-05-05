import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'

function Snapshots({ match }) {
    useEffect(() => {
        fetchItems();
        //console.log(match);
    }, []);

    const [items, setItem] = useState([{}]);
    const fetchItems = async () => {
        const fetchItem = await fetch(
            `http://127.0.0.1:5000/users/${match.params.id}/snapshots`);
        const items = await fetchItem.json();

        //console.log(items);
        setItem(items);
    };


    return (
        <div>
            <h1>snapshots</h1>
            {items.map(item => (
                <h3 key={item.timestamp}>Snapshot ID:
                    <Link to={`/users/${match.params.id}/snapshots/${item.timestamp}`}> {item.timestamp}</Link>
                </h3>
            ))}
        </div>
    );
}

export default Snapshots;