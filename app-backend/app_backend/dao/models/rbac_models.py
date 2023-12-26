from sqlmodel import Field, SQLModel, Relationship
from .base_model import BaseModel
from typing import Optional, List
from sqlalchemy_utils import EmailType, PasswordType
from sqlalchemy import Column


class Directory(BaseModel, table=True):
    name: str
    owner: str = Field(sa_column=Column(EmailType))
    capabilties: List['Capability'] = Relationship(back_populates="directory")
    roles: List['Role'] = Relationship(back_populates='directory')
    users: List['User'] = Relationship(back_populates='directory')


class RoleCapability(SQLModel, table=True):
    cap_id: int = Field(
        default=None, foreign_key='capability.id', primary_key=True)
    role_id: int = Field(default=None, foreign_key='role.id', primary_key=True)


class UserRole(SQLModel, table=True):
    user_id: int = Field(default=None, foreign_key='user.id', primary_key=True)
    role_id: int = Field(default=None, foreign_key='role.id', primary_key=True)


class Capability(BaseModel, table=True):
    name: str
    dir_id: int = Field(default=None, foreign_key="directory.id")
    description: Optional[str]
    directory: Directory = Relationship(back_populates="capabilities")
    roles: list['Role'] = Relationship(back_populates='capabilities')


class Role(BaseModel, table=True):
    name: str
    description: str
    dir_id: int = Field(default=None, foreign_key='directory.id')
    capabilities: List[Capability] = Relationship(
        back_populates='roles', link_model=RoleCapability)
    directory: Directory = Relationship(back_populates='roles')
    users: list['User'] = Relationship(back_populates="roles")


class User(BaseModel, table=True):
    email: str = Field(sa_column=Column(EmailType))
    password: str = Field(sa_column=Column(
        PasswordType(length=8, max_length=20)))
    dir_id: int = Field(default=None, foreign_key="directory.id")
    directroy: Directory = Relationship(back_populates='users')
    roles: List[Role] = Relationship(
        back_populates='users', link_model=UserRole)
