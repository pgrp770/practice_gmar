from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .class_model import ClassModel
from .teacher import Teacher
from .student_profile import StudentProfile
from .student_lifestyle import StudentLifestyle
from .student_performance import StudentPerformance