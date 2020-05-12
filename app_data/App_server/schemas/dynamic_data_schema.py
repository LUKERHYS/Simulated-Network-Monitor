from utils.ma import ma
from models.dynamic_data import DynamicData

class DynamicDataSchema(ma.Schema):
    class Meta:
        fields = ('id','time_stamp', 'upload_speed', 'download_speed', 'active_connection')

dynamic_data_schema = DynamicDataSchema(many=True)
