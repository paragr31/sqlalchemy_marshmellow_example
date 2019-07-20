from marshmallow import Schema, fields, validates, pre_dump, pre_load, post_dump, post_load
import json


class RFC(Schema):
    agora_name = fields.String(required=True, allow_none=False)
    agora_region = fields.Method('get_agora_region', required=True)
    ase_upgrade_by = fields.Method('get_upgrade_by', required=True)
    iq_upgrade_by = fields.Method('get_upgrade_by', required=True)
    # start_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S', required=True)

    @pre_load(pass_many=False)
    def format_date(self, data):
        print "Called format_date function in preload. Data = %s" % (data)

    # @validates('start_date')
    # def validate_start_date(self, data):
    #     print("start date=", data['start_date'])

    def get_agora_region(self, obj):
        if obj['agora_name'][:2] == "AM":
            return "AMER"
        elif obj['agora_name'][:2] == "UK":
            return "EMEA"
        else:
            return "APAC"
            
    def get_upgrade_by(self, obj):
        if obj['agora_name'][:2] == "AM":
            return "IRMA"
        elif obj['agora_name'][:2] == "UK":
            return "IRMA"
        else:
            return "DBA"

if __name__ == "__main__":
    serializer = RFC()
    rfc = dict(agora_name="UKPRIMEP01", start_date='2019-05-02 10:45:20')
    # rfc = dict(agora_name="UKPRIMEP01")
    result = json.loads(json.dumps(serializer.dump(rfc)))
    errors = serializer.validate(result[0])
    if errors:
        print errors
    else:
        print result[0]
