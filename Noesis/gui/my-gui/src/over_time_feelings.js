import React, {Component} from "react";
import {Bar, Line, Pie} from 'react-chartjs-2';

class OverTimeChart extends Component {
    constructor(props){
        super(props);
        this.state = {
            chartData:props.chartData
        }
    }

    static defaultProps = {
        displayTitle:true,
        displayLegend: true,
        legendPosition:'top',
        location:'City'
    }

    render(){
        console.log(this.props.chartData)
        return (
            <div>
                    <Line
                        data={this.props.chartData}
                        height={450}
                        width={600}
                        options={{
                            title:{
                                display:'{true}}',
                                text:'Feelings over time',
                                fontSize:25
                            },
                            legend:{
                                display:this.props.displayLegend,
                                position:'top'
                            },
                            scales: {
                                xAxes: [{
                                    type: 'time',
                                    time: {
                                        unit: 'minute'
                                    }
                                }]
                            },
                            responsive: false,
                            maintainAspectRatio: true,
                        }}
                    />
            </div>
        )
    }
}

export default OverTimeChart;