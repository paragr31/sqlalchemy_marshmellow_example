import sqlalchemy as sa
from sqlalmm_db import Base
from datetime import datetime

class RFC(Base):
    __tablename__ = "change_request"
    __table_args__ = {'extend_existing': True}
    rfc = sa.Column(sa.String(250), nullable=False, primary_key=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=False)
    created_on = sa.Column(sa.TIMESTAMP, nullable=False, default=datetime.now())
    sa.UniqueConstraint(rfc, name='unique_rfc')
