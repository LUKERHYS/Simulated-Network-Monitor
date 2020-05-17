from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from utils.db import Base

class StaticData(Base):
    __tablename__ = 'static_data'
    id = Column(Integer, primary_key = True)
    host_name = Column(String(255))
    device_type = Column(String(255))
    operating_system = Column(String(255))
    mac_address = Column(String(255), unique=True)
    ip_address = Column(String(255))
    snap_shots = relationship('DynamicData', back_populates='static_data')