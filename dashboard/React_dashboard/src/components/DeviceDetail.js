import React, {Component} from 'react';
import TotalDataChart from "./TotalDataChart";

class DeviceDetail extends Component {
    constructor(props) {
        super(props);
        this.state = {
            chartData: [['Time', 'Upload Mbs', 'Download Mbs']],
            open: false,
        }
        this.togglePanel = this.togglePanel.bind(this);
    }

    componentDidMount() {
        this.plotData() 
    }

    togglePanel(e){
        this.setState({open: !this.state.open})
    }

    plotData() {
        let newChartData = ['']
        this.props.snap_shots.map(timeStamp => {
        newChartData.push(timeStamp.upload_speed)
        newChartData.push(timeStamp.download_speed)
        this.state.chartData.push(newChartData)
        newChartData = ['']    
        })
    }

    render() {
        return (
                <div>
                    <div onClick={(e)=> this.togglePanel(e)} className ='header'>
                    
                    <div className="device-title-bar">
                        <h3>{this.props.deviceName}</h3>
                        <div className={this.props.activeConnection ? "connection-light-connected" : "connection-light-disconnected" }></div>   
                        </div>
                    
                    </div> 
                    {
                    this.state.open? (
                    <div className='device-list-content'> 
                    <div>
                    <p>Device: {this.props.deviceType}</p>
                    <p>IP Address: {this.props.ipAddress}</p> 
                    <p>MAC Address: {this.props.macAddress}</p> 
                    <p>OS: {this.props.operatingSystem}</p>
                    <p>Connection Status: {this.props.activeConnection ? "Connected" : "Disconnected"}</p>
                    <p>Upload Speed: {this.props.uploadSpeed}</p>
                    <p>Download Speed: {this.props.downloadSpeed}</p>
                    </div>
                    <div>
                    
                    <TotalDataChart chartData={this.state.chartData} /> </div>
                    </div>
                    )
                    :null 
                    }
                </div>
        );
    }
}






export default DeviceDetail;
