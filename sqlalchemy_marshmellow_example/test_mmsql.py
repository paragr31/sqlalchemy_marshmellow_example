from sqlalmm_db.schemas import RFCSchema, AttachmentSchema
from sqlalmm_db import Session, Base, engine

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

rfc_schema = RFCSchema()
attach_schema = AttachmentSchema()
data = {
    'rfc': 'RFC2345334',
    'summary': 'Test marshmellow ',
    'description': 'Test'
}
attachments = [
    {
        'document_name': 'test1',
        'document_file': 'C:\parag\test1.sql'
    },
    {
        'document_name': 'test2',
        'document_file': 'C:\parag\test2.sql'
    }
]
validation = rfc_schema.validate(data, session=Session)
if not validation:
    rfc = rfc_schema.load(data, session=Session)
    for att in attachments:
        attach = attach_schema.load(att, session=Session)
        rfc.data.rfc_attachments.append(attach.data)
    Session.add(rfc.data)
    Session.commit()
else:
    print validation

