import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import 'react-table-v6/react-table.css'
import Animate from 'animate.css-react'
import './styles/animate.css'
import $ from 'jquery'
import { findDOMNode} from "react-dom";

class Home extends Component{
    constructor(props) {
        super(props)
        this.state={}
    }

    componentDidMount() {
        $('button').on('click', function () {
            var effects = 'animated flipOutX';
            var effectsEnd = 'animationend oAnimationEnd mozAnimationEnd webkitAnimationEnd';
            $(this).addClass(effects).one(effectsEnd, function () {
                $(this).removeClass(effects);
            });
            setTimeout(function(){document.location.href="http://127.0.0.1:3000/users";}, 700);
        });
    }

    handleHover(){
        $('button').on('click', function () {
            var effects = 'animated flipOutX';
            var effectsEnd = 'animationend oAnimationEnd mozAnimationEnd webkitAnimationEnd';
            $(this).addClass(effects).one(effectsEnd, function () {
                $(this).removeClass(effects);
            });
        });
    }

    render() {

        return (
            <div>
                <h1 className={"welcome animated fadeIn"}>Welcome</h1>
                <button className={"button-style animated tada"} >Start</button>
            </div>
        )
    }
}

export default Home;