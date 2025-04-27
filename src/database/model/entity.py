from sqlalchemy import Column, Integer, Boolean, Text, Numeric, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

# class TextIntent(Base):
#     __tablename__ = 'text_intent'
    
#     text_intent_id = Column(Integer, primary_key=True, autoincrement=True)
#     text_id = Column(Integer, ForeignKey('text.text_id'), nullable=False)
#     expert_id = Column(Integer, ForeignKey('expert.expert_id'), nullable=False)
#     intent_id = Column(Integer, ForeignKey('intent.intent_id'), nullable=False)
#     is_true = Column(Boolean, nullable=False, default=True)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)

#     # text = relationship("Text")
#     # expert = relationship("Expert")
#     # intent = relationship("Intent")


class Expert(Base):
    __tablename__ = 'expert'

    expert_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=True)
    phone = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)


class IntentType(Base):
    __tablename__ = 'intent_type'

    type_id = Column(Integer, primary_key=True, autoincrement=True)
    expert_id = Column(Integer, ForeignKey('expert.expert_id'), nullable=False)
    name = Column(Text, nullable=True)
    frequency = Column(Integer, nullable=True, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)


class Intent(Base):
    __tablename__ = 'intent'

    intent_id = Column(Integer, primary_key=True, autoincrement=True)
    expert_id = Column(Integer, ForeignKey('expert.expert_id'), nullable=False)
    name = Column(Text, nullable=True)
    type_id = Column(Integer, nullable=False)
    frequency = Column(Integer, nullable=True)
    k_fleiss_coherence = Column(Numeric, nullable=True, default=None)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
