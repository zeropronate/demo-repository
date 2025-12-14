from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Class(Base):
    __tablename__ = "Class"
    class_id = Column(Integer, primary_key=True, index=True),
    Class_name = Column(String, nullable=False),
    Class_sec = Column(String, nullable=False),
    Class_stream = Column(String, nullable=False),
    class_avgno = Column(Integer, nullable=True),
    class_no_of_stu = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="class_mapper", cascade="all, delete-orphan")


class Student(Base):
    __tablename__ = "Student"
    student_id = Column(Integer, primary_key=True, index=True),
    student_name = Column(String, nullable=False),
    student_sec = Column(String, nullable=False),
    student_class = Column(Integer, nullable=False),
    student_marks = Column(Float, nullable=True),
    student_chunni = Column(String, nullable=False),

    class_id = Column(Integer, ForeignKey("Class.class_id", ondelete="CASCADE"), nullable=False),

    class_mapper = relationship("Class", back_populates ="class")

