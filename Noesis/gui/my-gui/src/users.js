import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import 'react-table-v6/react-table.css'
import ReactTable from "react-table-v6";
import { useHistory } from "react-router-dom";
import './styles/snapshots.scss';
import $ from "jquery";
import {getUsers} from "./connect_api";


class Users extends Component{

    constructor(props) {
        super(props);
        this.state={}
    }

    async componentDidMount() {
        await this.fetchItems();

    }

    fetchItems = async () => {
        const {match} = this.props;
        console.log(getUsers())
        const items = await getUsers();
        this.setState({items})

    };



    render()
    {
        const {items}  = this.state;
        const {match} = this.props;

        const columns = [{
            Header: 'User Id',
            accessor: 'user_id', // String-based value accessors!

            Cell: props => <a className={"navStyle"} onClick={"handleClick"} href={`/users/${props.original.user_id}`}>{props.original.user_id}</a>
        }, {
            Header: 'User Name',
            accessor: 'user_name',
        }
        ]

        return (

            <div className={"table-header animated fadeInLeft"}>
                <h1 className={"titles"}>Users</h1>
                {<ReactTable
                    data={items}
                    columns={columns}
                    defaultPageSize={10}
                    defaultSortDesc={true}
                    defaultSorted={[{ // the sorting model for the table
                        id: 'user_id',
                        desc: false
                    }]}
                    minRows={0}
                />}
            </div>
        );
    }
}

export default Users;