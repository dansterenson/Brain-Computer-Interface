import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import ReactTable from "react-table-v6";


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

    onButtonClickHandler = param => e => {
        window.alert(param);
    };

    render() {
        const {items}  = this.state;
        const {match} = this.props
        console.log({match})
        if (!items)
            return  null;

        const columns = [{
            Header: 'Image Width',
            accessor: 'width',
        }, {
            Header: 'Image Height',
            accessor: 'height', // String-based value accessors!
        }, {
            Header: 'Image Path',
            accessor: 'parsed_path',
            Cell: props => <div className={"navStyle"}>
                <button onClick={this.onButtonClickHandler(props.original.parsed_path)}>view file path</button>
            </div>
        }, {
            Header: 'Image',
            Cell: props => <a className={"navStyle"} href={`http://127.0.0.1:3000/users/${match.params.id}/snapshots/${match.params.snapshot}/color_image/data`}>View Image</a>
        },
        ]
        return (
            <div className={"table-header"}>
                <h1>Color Image</h1>
                {<ReactTable
                    data={items}
                    columns={columns}
                    defaultPageSize={1}
                />}
            </div>
        );
    }
}

export default ColorImage;