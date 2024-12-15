"""
id,first_name,last_name,age,address
1,Tammy,Mccoy,27,74772 Brown Meadow Suite 925
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from sql_menegment_app.sql_db.models import Base


class StudentProfile(Base):
    __tablename__ = 'student_profiles'
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    address = Column(String)

    life_style = relationship("StudentLifeStyle", back_populates="student_profile")
    performance = relationship("StudentPerformance", back_populates="student_profile")