from utils.ma import ma
from models.device import Device

class DeviceSchema(ma.Schema):
    class Meta:
        fields = ('id','host_name', 'device_type', 'operating_system', 'mac_address', 'ip_address', 'upload_speed', 'download_speed', 'active_connection')

device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)

