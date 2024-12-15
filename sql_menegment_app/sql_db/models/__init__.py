from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .class_model import ClassModel
from .teacher import Teacher
