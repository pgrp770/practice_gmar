"""
    {
      "id": "CS-786",
      "course_name": "Data Structures",
      "section": 1,
      "department": "Computer Science",
      "semester": "Spring 2024",
      "room": "Building A-204",
      "schedule": "Tue 14:00",
      "teacher_id": "CS-3307"
    }
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from sql_menegment_app.sql_db.models import Base


class ClassModel(Base):
    __tablename__ = 'classes'
    id = Column(String, primary_key=True)
    course_name = Column(String)
    section = Column(Integer)
    department = Column(String)
    semester = Column(String)
    room = Column(String)
    schedule = Column(String)

    teacher_id = Column(String, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="classes")