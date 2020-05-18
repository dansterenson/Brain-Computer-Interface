import React, {Component} from "react";
import {Bar, Line, Pie} from 'react-chartjs-2';

class Chart extends Component {
    constructor(props){
        super(props);
        this.state = {
            chartData:props.chartData
        }
    }

    static defaultProps = {
        displayTitle:true,
        displayLegend: false,
        legendPosition:'right',
        location:'City'
    }

    render(){
        console.log(this.props.chartData)
        return (
            <div>
                <div className={"bchart"}>
                    <Bar
                        data={this.props.chartData}
                        height={450}
                        width={600}
                        options={{
                            title:{
                                display:'',
                                text:'Feelings',
                                fontSize:25
                            },
                            legend:{
                                display:this.props.displayLegend,
                                position:'right'
                            },
                            responsive: true,
                            maintainAspectRatio: false,
                        }}
                    />
                </div>
                <div className={"pchart"}>
                    <Pie
                        data={this.props.chartData}
                        height={400}
                        width={500}
                        options={{
                        responsive: false,
                        maintainAspectRatio: false,
                        }}
                    />
                </div>
            </div>
        )
    }
}

export default Chart;