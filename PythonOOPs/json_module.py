import json
emp = { 'emp': 'Niharika',
        'age': 32,
        'salary': 1000,
        'ismarried': True


}

print(emp)
json_string = json.dumps(emp,indent=4,sort_keys=True)
print(json_string)
with open('empfile.json','w') as f:
    json.dump(emp,f,indent=4,sort_keys=True)



# json to python dictionary 

emp_json = '''
{
    "age": 32,
    "emp": "Niharika",
    "ismarried": true,
    "salary": 1000
}
'''
print(emp_json)
pystring = json.loads(emp_json)
print(type(pystring))

for k,v in pystring.items():
    print(k,v)

with open('empfile.json','r') as f:
    empdict1 = json.load(f)
 
for k,v in empdict1.items():
    print(k,v)    



