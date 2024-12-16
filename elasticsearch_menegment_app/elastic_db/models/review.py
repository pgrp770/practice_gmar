from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict


@dataclass
class Review:
   review_id: str
   content: str
   score: int
   thumbs_up_count: int
   review_created_version: str
   date_time: datetime
   app_version: str
   student_id: int
