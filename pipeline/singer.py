columns = ('id','name', 'age', 'has_children')
users = {(1,'Adrian',32, False),
         (2,'Ruanne',28, False),
         (3,'Hillary',29, True),}
json_schema = {
    'properties': {'age': {'maximum': 130,
                           'minimum':1,
                           'type':'integer'},
                   'has_children': {'type':'boolean'},
                   'id':{'type':'integer'},
                   'name':{'type':'string'}},
    '$id': 'http://yourdomain.com/schemas/my_user_schema.json',
    '$schema': 'http://json-schema.org/draft-07/schema#'
}

# import singer
# singer.write_schema(schema=json_schema,
#                     stream_name='DC_employees',
#                     key_properties=['id'])

import json
json.dumps(json_schema['properties']['age'])

# with open('foo.json','w') as fh:
#     json.dump(obj=json_schema, fp=fh)

singer.write_record(stream_name='DC_employees', record=dict(zip(columns,users.pop())))
singer.write_records(stream_name='foo', record=...)

fixed_dict={'type':'RECORD','stream':'DC_employees'}
record_msg={**fixed_dict,'record':dict(zip(columns, users.pop()))}
print(json.dumps(record_msg))