from sqlmodel import SQLModel, Field
from datetime import datetime


class BaseModel(SQLModel, table=False):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default=datetime.utcnow, nullable=False)
