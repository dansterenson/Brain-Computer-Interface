import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import './styles/snapshots.scss';
import {getSnapshotResult, getSnapshotResultDataUrl} from "./connect_api";
import ReactTable from "react-table-v6";

class DepthImage extends Component{

    constructor(props) {
        super(props);
        this.state={}
    }

    async componentDidMount() {
        await this.fetchItems();
    }

    fetchItems = async () => {
        const {match} = this.props;
        const items = await getSnapshotResult(match.params.id, match.params.snapshot, "depth_image")
        const image_src = await getSnapshotResultDataUrl(match.params.id, match.params.snapshot, 'depth_image')
        this.setState({items})
        this.setState({image_src})

    };

    onButtonClickHandler = param => e => {
        window.alert(param);
    };

    render() {
        const {match} = this.props
        const {items}  = this.state;
        const {image_src} = this.state;
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
        },
        ]

        return (
            <div className={"table-header"}>
                <h1>depth Image</h1>
                {<ReactTable
                    showPagination={false}
                    data={items}
                    columns={columns}
                    defaultPageSize={1}
                />}
                <view>
                    <img className={"animated fadeIn color-image"} src={image_src}
                         resizeMode='contain'
                         style={{maxHeight: 480, maxWidth: 640}}
                    />
                </view>
            </div>
        );
    }
}


export default DepthImage;