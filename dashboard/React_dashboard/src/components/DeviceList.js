import React from 'react';
import DeviceDetail from './DeviceDetail.js'

const DeviceList = (props) => {
    const deviceItems = props.devices.map(device => {
        return (
            <DeviceDetail key={device.ip_address}
            id={device.id} 
            deviceName={device.host_name}
            deviceType={device.device_type}
            ipAddress={device.ip_address}
            macAddress={device.mac_address}
            operatingSystem={device.operating_system}
            activeConnection={device.snap_shots[device.snap_shots.length - 1].active_connection}
            uploadSpeed={device.snap_shots[device.snap_shots.length - 1].upload_speed}
            downloadSpeed={device.snap_shots[device.snap_shots.length - 1].download_speed}
            snap_shots={device.snap_shots}
            />
        )
    })
        
    return (
        <ul>
        {deviceItems}
        </ul>
    )
     
}

export default DeviceList;
