from marshmallow_sqlalchemy import ModelSchema
from sqlalmm_db import Session
from .models import RFC, Attachments


class BaseSchema(ModelSchema):
    class Meta:
        sqla_session = Session


class RFCSchema(BaseSchema):
    class Meta:
        model = RFC


class AttachmentSchema(BaseSchema):
    class Meta:
        model = Attachments