import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import 'react-table-v6/react-table.css'
import ReactTable from "react-table-v6";
import { useHistory } from "react-router-dom";
import Moment from 'react-moment';
import Chart from "./chart";
import OverTimeChart from "./over_time_feelings";



class User extends Component{

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
            `http://127.0.0.1:5000/users/${match.params.id}`);
        const items = await fetchItem.json();
        this.setState({user: items.user})
        console.log(items)
        const exhaustion = Object.keys(items.feelings).map(m => (items.feelings[m].feelings_at_timestamp.exhaustion));
        const happiness = Object.keys(items.feelings).map(m => (items.feelings[m].feelings_at_timestamp.happiness));
        const hunger = Object.keys(items.feelings).map(m => (items.feelings[m].feelings_at_timestamp.hunger));
        const thirst = Object.keys(items.feelings).map(m => (items.feelings[m].feelings_at_timestamp.thirst));
        const timestamps = Object.keys(items.feelings).map(m => (items.feelings[m].timestamp));

        const chartData1 = {
            labels: timestamps,
            datasets: [
                {
                    label: 'Hunger',
                    data: hunger,
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.6)',
                    ]
                },
                {
                    label: 'Exhaustion',
                    data: exhaustion,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                    ],
                },
                {
                    label: 'Happiness',
                    data: happiness,
                    backgroundColor: [
                        'rgba(255, 206, 86, 0.6)',
                    ]
                },

                {
                    label: 'Thirst',
                    data: thirst,
                    backgroundColor: [
                        'rgba(255, 159, 64, 0.6)',
                    ]
                }

            ]
        }
        this.setState({exhaustion: chartData1})

    };



    render()
    {
        const {match} = this.props;
        const columns = [{
            Header: 'User Id',
            accessor: 'user_id', // String-based value accessors!
        }, {
            Header: 'User Name',
            accessor: 'user_name',
        }, {
            Header: 'User Birthday',
            Cell: props => <td><Moment format="MMMM Do YYYY" unix>{props.original.birthday}</Moment></td>
        }, {
            Header: 'User Gender',
            accessor: 'gender',
        }, {
            Header: 'snapshots',
            Cell: props => <a className={"navStyle"} href={`/users/${match.params.id}/snapshots/`}>View Snapshots</a>
        }
        ]

        return (

            <div className={"table-header "}>
                <h1 className={"titles"}>User Details</h1>
                {<ReactTable
                    data={this.state.user}
                    columns={columns}
                    defaultPageSize={5}
                    minRows={0}
                    showPagination={false}
                    />}
                <div className={"feelings-over-time"}>
                    <OverTimeChart chartData={this.state.exhaustion}/>
                </div>

            </div>
        );
    }
}

export default User;