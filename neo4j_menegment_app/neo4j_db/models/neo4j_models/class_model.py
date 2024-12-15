from dataclasses import dataclass


@dataclass
class ClassModel:
    id: str
    course_name: str
    section: int
    department: str
    semester: str
    room: str
    schedule: str
    teacher_id: str
