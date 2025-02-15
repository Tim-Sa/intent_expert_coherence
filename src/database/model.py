from sqlalchemy import Column, Integer, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class TextIntent(Base):
    __tablename__ = 'text_intent'
    
    text_intent_id = Column(Integer, primary_key=True, autoincrement=True)
    text_id = Column(Integer, ForeignKey('text.text_id'), nullable=False)
    expert_id = Column(Integer, ForeignKey('expert.expert_id'), nullable=False)
    intent_id = Column(Integer, ForeignKey('intent.intent_id'), nullable=False)
    is_true = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)

    text = relationship("Text")
    expert = relationship("Expert")
    intent = relationship("Intent")

