import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import 'react-table-v6/react-table.css'
import ReactTable from "react-table-v6";
import { useHistory } from "react-router-dom";



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
        console.log({items})
        if (!items)
            return  null;

        const columns = [{
            Header: 'Snapshot Id',
            accessor: 'snapshot_id', // String-based value accessors!
        }, {
            Header: 'Snapshot Date-Time',
            accessor: 'date_time',
        }, {
            Header: 'Available Results',
            accessor: 'available_results',
            Cell: props => props.original.available_results.map(item=><li key={item}>
                <Link to={`/users/${match.params.id}/snapshots/${match.params.snapshot}/${item}`}> {item}</Link>
            </li>)
        },
        ]
        return (
            <div className={"table-header"}>
                <h1>Snapshot Details</h1>
                {<ReactTable
                    data={items}
                    columns={columns}
                    defaultPageSize={1}
                />}
            </div>
        );
    }
}


export default Snapshot;