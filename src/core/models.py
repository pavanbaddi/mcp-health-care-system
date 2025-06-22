from sqlalchemy import Column, String
from src.settings import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime
import uuid

class BaseModel(Base):
    __abstract__ = True    
    
    id = Column(String(255), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    
    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_dict()})"