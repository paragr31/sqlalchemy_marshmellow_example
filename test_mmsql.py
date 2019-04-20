from sqlalmm_db.schemas import RFCSchema
from sqlalmm_db import Session, Base, engine

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

rfc_schema = RFCSchema()
data = {
    'rfc': 'RFC23453',
    'summary': 'Test marshmellow',
}
validation = rfc_schema.validate(data, session=Session)
if not validation:
    rfc = rfc_schema.load(data, session=Session)
    Session.commit()
else:
    print validation

