from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base

class ProcessedFile(Base):
    __tablename__ = "processed_files"

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("static_files.id"))
    folder_path = Column(String(255), index=True)  # 指定长度
    status = Column(String(50), default="Pending")  # 指定长度
    result_url = Column(String(255), nullable=True)  # 指定长度

    static_file = relationship("StaticFile", back_populates="processed_files")
    projects = relationship("Project", back_populates="processed_file")