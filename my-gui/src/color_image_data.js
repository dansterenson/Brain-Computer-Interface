import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';


class ColorImageData extends Component{

    constructor(props) {
        super(props);
        this.state={}
    }


    render() {
        const {match} = this.props
        return (
            <view>
                <img src={`http://127.0.0.1:5000/users/${match.params.id}/snapshots/${match.params.snapshot}/color_image/data`}
                     resizeMode='contain'
                     style={{maxHeight: 480, maxWidth: 640}}
                />
            </view>
        );
    }
}


export default ColorImageData;