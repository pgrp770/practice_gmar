"""
student_id,course_name,current_grade,attendance_rate,assignments_completed,missed_deadlines,participation_score,midterm_grade,study_group_attendance,office_hours_visits,extra_credit_completed
1,English Literature,79.03,73.89,10,2,78.58,77.69,8,5,1
"""
from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from sql_menegment_app.sql_db.models import Base


class StudentPerformance(Base):
    __tablename__ = 'student_performances'

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    current_grade = Column(Float)
    attendance_rate = Column(Float)
    assignments_completed = Column(Float)
    missed_deadlines = Column(Float)
    participation_score = Column(Float)
    midterm_grade = Column(Float)
    study_group_attendance = Column(Integer)
    office_hours_visits = Column(Integer)
    extra_credit_completed = Column(Integer)

    student_id = Column(Integer, ForeignKey('student_profiles.student_id'))
    student_profile = relationship('StudentProfile', back_populates='life_style')

