from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from utils.db import Base

class DynamicData(Base):
    __tablename__ = 'dynamic_data'
    id = Column(Integer, primary_key = True)
    static_data_id = Column(Integer, ForeignKey('static_data.id'), nullable=False)
    static_data = relationship('StaticData', back_populates='snap_shots')
    time_stamp = Column(String(255))
    upload_speed = Column(Integer)
    download_speed = Column(Integer)
    active_connection = Column(Boolean)