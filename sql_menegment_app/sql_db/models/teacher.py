"""
"id": "CS-9416",
      "name": "Jeffery Arnold",
      "department": "Computer Science",
      "title": "Professor",
      "office": "Building B-332",
      "email": "cs-9416@university.edu"
"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from sql_menegment_app.sql_db.models import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(String, primary_key=True)
    name = Column(String)
    department = Column(String)
    title = Column(String)
    office = Column(String)
    email = Column(String)

    classes = relationship("ClassModel", back_populates="teacher")