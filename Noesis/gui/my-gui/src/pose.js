import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import ReactTable from "react-table-v6";
import {getSnapshotResult} from "./connect_api";
import $ from "jquery";


class Pose extends Component{

    constructor(props) {
        super(props);
        this.state={}
    }

    async componentDidMount() {
        const {match} = this.props
        await this.fetchItems();
    }

    fetchItems = async () => {
        const {match} = this.props;
        const items = await getSnapshotResult(match.params.id, match.params.snapshot, "pose")
        this.setState({items})
        console.log({items})
    };

    onButtonClickHandler = param => e => {
        window.alert(param);
    };

    render() {
        const {items}  = this.state;
        const {match} = this.props
        if (!items)
            return  null;

        const col_translation = [{
            Header: 'X',
            accessor: 'translation[0]',
        },{
            Header: 'Y',
            accessor: 'translation[1]',
        },{
            Header: 'Z',
            accessor: 'translation[2]',
        },
        ]

        const col_rotation = [{
            Header: 'X',
            accessor: 'rotation[0]',
        },{
            Header: 'Y',
            accessor: 'rotation[1]',
        },{
            Header: 'Z',
            accessor: 'rotation[2]',
        },{
            Header: 'W',
            accessor: 'rotation[3]',
        }
        ]
        return (
            <div className={"table-header"}>
                <h1>User Position</h1>
                <h3>Translation</h3>
                {<ReactTable
                    showPagination={false}
                    data={items}
                    columns={col_translation}
                    defaultPageSize={1}
                />}
                <h3>Rotation</h3>
                {<ReactTable
                    showPagination={false}
                    data={items}
                    columns={col_rotation}
                    defaultPageSize={1}
                />}
            </div>
        );
    }
}

export default Pose;
