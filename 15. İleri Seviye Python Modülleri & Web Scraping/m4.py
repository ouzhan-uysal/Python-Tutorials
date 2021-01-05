# JSON Modülü => Ortak veri taşıma objesi

import json

"""
# String Type:
person_string = '{"name":"Oğuzhan","languages":["python", "java"]}'

# JSON String to Dict:
r = json.loads(person_string)
r = r["languages"]
print(type(r))
print(r)
"""

"""
# Json dosyasından data okuma
with open("m4.json", encoding="utf-8") as mj:
    data = json.load(mj)
    print(data["languages"])
"""
# ------------------------------------------------------------
"""
# Dictinary Type
person_dict = {
    "name": "Oğuzhan",
    "languages": ["Python", "Java"]
}
## Dict to JSON String
# r = json.dumps(person_dict)
# print(r)
# print(type(r))
with open("m4.json", "w", encoding="utf-8") as mj:
    json.dump(person_dict, mj)  # json modülünü kullanarak mj dosyasının içerisine person_dict'deki bilgileri dump ettik.
"""

# String Type:
person_string = '{"name":"Oğuzhan","languages":["python", "java"]}'

# Dictinary Type:
person_dict = {
    "name": "Oğuzhan",
    "languages": ["Python", "Java"]
}
# x
person_dict = json.loads(person_string)

r = json.dumps(person_dict, indent=4, sort_keys=True)   # Json formatının düzgün bir şekilde yazılması için gerekli

print(person_dict)
print(r)