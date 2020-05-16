import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import 'react-table-v6/react-table.css'
import ReactTable from "react-table-v6";
import { useHistory } from "react-router-dom";
import './styles/snapshots.scss';
import Moment from 'react-moment';


class Snapshots extends Component{

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
            `http://127.0.0.1:5000/users/${match.params.id}/snapshots`);
        const items = await fetchItem.json();
        this.setState({items})
    };



    render()
    {
        const {items}  = this.state;
        const {match} = this.props;
        const columns = [{
            Header: 'Snapshot Id',
            accessor: 'timestamp', // String-based value accessors!
            Cell: props => <a className={"navStyle"} href={`/users/${match.params.id}/snapshots/${props.original.timestamp}`}>{props.original.timestamp}</a>
        }, {
            Header: 'Snapshot Date-Time',
            accessor: 'datetime',
            Cell: props => <td><Moment format="MMMM Do, h:mm:ss a" unix>{props.original.datetime}</Moment></td>
        }
        ]

        return (
            <div>
                <h1 className={"page-header table-header animated fadeInLeft "}>Snapshots</h1>
                {<ReactTable className={"ReactTable animated fadeInLeft "}
                    showPageSizeOptions={true}
                    pageSizeOptions={[10, 20, 50, 100]}
                    defaultPageSize={7}
                    defaultSortDesc={true}
                    defaultSorted={[{ // the sorting model for the table
                        id: 'datetime',
                        desc: false
                    }]}
                    defaultResized={[23]}
                    data={items}
                    columns={columns}
                />}
            </div>
        );
    }
}

export default Snapshots;