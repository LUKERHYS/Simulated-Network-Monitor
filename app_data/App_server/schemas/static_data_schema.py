from utils.ma import ma
from models.static_data import StaticData
from schemas.dynamic_data_schema import DynamicDataSchema

class StaticDataSchema(ma.Schema):

    class Meta:
        fields = ('id','host_name', 'device_type', 'operating_system', 'mac_address', 'ip_address', 'snap_shots')
    
    snap_shots = ma.Nested(DynamicDataSchema(many=True))
    
static_data_schema = StaticDataSchema(many=True)