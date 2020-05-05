import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';


class Feelings extends Component{

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
            `http://127.0.0.1:5000/users/${match.params.id}/snapshots/${match.params.snapshot}/feelings`);
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
                <h1>Feelings</h1>
                {items.map(item => (
                    <h3 key={item.snapshot_id}>
                        Exaustion: {item.exhaustion} <br></br>
                        Happiness: {item.happiness} <br></br>
                        Hunger: {item.hunger} <br></br>
                        Thirst: {item.thirst} <br></br>
                    </h3>
                ))}
            </div>
        );
    }
}


export default Feelings;