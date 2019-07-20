import sqlalchemy as sa
from sqlalmm_db import Base
from datetime import datetime


class RFC(Base):
    __tablename__ = "change_request"
    __table_args__ = {'extend_existing': True}
    rfc = sa.Column(sa.String(250), nullable=False, primary_key=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=False)
    created_on = sa.Column(sa.TIMESTAMP, nullable=False, default=datetime.now(), onupdate=datetime.now())
    sa.UniqueConstraint(rfc, name='unique_rfc')


class Attachments(Base):
    __tablename__ = "rfc_attachments"
    __table_args__ = {'extend_existing': True}
    id = sa.Column(sa.Integer, primary_key=True)
    document_name = sa.Column(sa.String(250), nullable=False)
    document_file = sa.Column(sa.String, nullable=False)
    rfc_number = sa.Column(sa.String, sa.ForeignKey('change_request.rfc'))
    
    change_request = sa.orm.relationship('RFC', back_populates='rfc_attachments')

RFC.rfc_attachments = sa.orm.relationship("Attachments", order_by=Attachments.id, back_populates="change_request")
