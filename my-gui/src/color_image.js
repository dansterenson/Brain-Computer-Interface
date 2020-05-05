import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';


class ColorImage extends Component{

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
            `http://127.0.0.1:5000/users/${match.params.id}/snapshots/${match.params.snapshot}/color_image`);
        const items = await fetchItem.json();
        this.setState({items})

    };

    render() {
        const {items}  = this.state;
        const {match} = this.props
        console.log(match);
        if (!items)
            return  null;
        return (
            <div>
                <h1>Color Image</h1>
                {items.map(item => (
                    <h3 key={item.snapshot_id}>
                        Image Height: {item.height} <br></br>
                        Image Width: {item.width} <br></br>
                        Image Path: {item.parsed_path} <br></br>
                        <Link to={`/users/${match.params.id}/snapshots/${match.params.snapshot}/color_image/data`}>Click here see Image</Link>
                    </h3>
                ))}
            </div>
        );
    }
}


export default ColorImage;