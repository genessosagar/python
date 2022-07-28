'''JSON - Java Script Object Notation'''
'''
Json        Python
object          dict
array           list
string          str
number(int)     int
number(real)    float
true            True
false           False
null            None
'''

import json

people_string = '''
{
    "people" : [
        {
            "name" : "David Vidya Sagar",
            "phone" : "1234-5678-90",
            "emails" : ["sagar@abc.com", "david@abc.com"],
            "has_license" : false
        },
        {
            "name" : "Neera Sitara",
            "phone" : "0987-6543-21",
            "emails" : null,
            "has_license" : true
        }
    ]
}
'''

data = json.loads(people_string)
print(data)
print(type(data))

for person in data['people']:
    print(person)

for person in data['people']:
    del person['phone']

new_str = json.dumps(data, indent=2, sort_keys=True)    # Sort keys will sort keys alphabetically
print(new_str)