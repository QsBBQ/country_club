from sqlalchemy import Table, Column, ForeignKey, DateTime, Integer, String
from sqlalchemy import Sequence

from sqlalchemy.orm import relationship, backref
# import for db base
# how to get this working? from country_club.db import Base
# from db import Base
import datetime

###
# May be seperate after imports are sorted.
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///country_club.sqlite')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))

Base = declarative_base()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)

###


class Administrator(Base):
    __tablename__ = "adminstrators"
    id = Column(Integer, Sequence("administrator_id"), primary_key=True)
    name = Column(String(50), nullable=True)
    username = Column(String(50), nullable=True)
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)


class ClubLocation(Base):
    __tablename__ = "club_locations"
    id = Column(Integer, Sequence("club_location_id"), primary_key=True)
    name = Column(String(50), nullable=True)
    description = Column(String(250))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)


class Residence(Base):
    __tablename__ = "residences"
    id = Column(Integer, Sequence("residence_id"), primary_key=True)
    name = Column(String(50))
    address = Column(String(50))
    description = Column(String(250))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)


class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, Sequence("member_id"), primary_key=True)
    name = Column(String(50), nullable=True)
    username = Column(String(50), nullable=True)
    note = Column(String(250))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
    # Relationships
    clubs = relationship("Club", secondary="member_club_join",
                           backref="backref_members",
                           cascade="all, delete-orphan",
                           single_parent=True)
    family_members = relationship("FamilyMember", backref=backref("members"),
                                  cascade="all, delete-orphan")


class FamilyMember(Base):
    __tablename__ = "family_members"
    id = Column(Integer, Sequence("family_id"), primary_key=True)
    name = Column(String(50), nullable=True)
    relation = Column(String(50), nullable=True)
    note = Column(String(250))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
    # Relationships
    member_id = Column(Integer, ForeignKey("members.id"))


class Club(Base):
    __tablename__ = "clubs"
    id = Column(Integer, Sequence("club_id"), primary_key=True)
    name = Column(String(50), nullable=True)
    description = Column(String(250))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
    # Club Relationships
    members = relationship("Member", secondary="member_club_join",
                         backref="backref_clubs", cascade="all, delete-orphan",
                         single_parent=True)


class MemberClubJoin(Base):
    """
    Join table for member and clubs
    """
    __tablename__ = "member_club_join"
    club_id = Column(Integer, ForeignKey("clubs.id"), primary_key=True)
    member_id = Column(Integer, ForeignKey("members.id"), primary_key=True)
    tag = Column(String(50))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
    # Relationships
    club = relationship("Club", backref="club_member_join")
    member = relationship("Member", backref="member_club_join")
