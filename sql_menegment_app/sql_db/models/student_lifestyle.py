"""
Student_ID,Study_Hours_Per_Day,Extracurricular_Hours_Per_Day,Sleep_Hours_Per_Day,Social_Hours_Per_Day,Physical_Activity_Hours_Per_Day,GPA,Stress_Level
1,6.9,3.8,8.7,2.8,1.8,2.99,Moderate
"""
from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from sql_menegment_app.sql_db.models import Base


class StudentLifestyle(Base):
    __tablename__ = 'student_lifestyles'

    id = Column(Integer, primary_key=True)
    study_hours_per_day = Column(Float)
    extracurricular_hours_per_day = Column(Float)
    sleep_hours_per_day = Column(Float)
    social_hours_per_day = Column(Float)
    physical_activity_hours_per_day = Column(Float)
    gpa = Column(Float)
    stress_level = Column(String)


    student_id = Column(Integer, ForeignKey('student_profiles.student_id'))
    student_profile = relationship('StudentProfile', back_populates='life_style')


