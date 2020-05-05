import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';


class Snapshot extends Component{

    constructor(props) {
        super(props);
        this.state={}
    }

    async componentDidMount() {
        await this.fetchItems();
    }

    fetchItems = async () => {
        const {match} = this.props;
        const fetchItem = await fetch(
            `http://127.0.0.1:5000/users/${match.params.id}/snapshots/${match.params.snapshot}`);
        const items = await fetchItem.json();
        this.setState({items})
    };

    render() {
        const {items}  = this.state;
        const {match} = this.props
        if (!items)
            return  null;
        return (
            <div>
                <h1>Snapshot Details</h1>
                {items.map(item => (
                    <h3 key={item.snapshot_id}>
                        Snapshot ID: {item.snapshot_id} <br></br>
                        Date-time: {item.date_time} <br></br>
                        Available Results:
                        {item.available_results.map(res => (
                            <li key={res}>
                                <Link to={`/users/${match.params.id}/snapshots/${item.snapshot_id}/${res}`}> {res}</Link>
                            </li>))}
                    </h3>
                ))}
            </div>
        );
    }
}


export default Snapshot;