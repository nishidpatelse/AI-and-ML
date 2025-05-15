from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()
engine = create_engine('sqlite:///interactions.db')
Session = sessionmaker(bind=engine)

class UserInteraction(Base):
    __tablename__ = 'interactions'
    id = Column(Integer, primary_key=True)
    query = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

def log_interaction(query):
    session = Session()
    interaction = UserInteraction(query=query)
    session.add(interaction)
    session.commit()
