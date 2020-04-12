import json
balance = 5000
marriage = False

name = input("name: ")
uid = int(input("id: "))
balance = input("balance: ")
p = input("partner: ")
if p=='n':
    partner = None
else:
    partner = p

data = {'name': name,
        'id': uid,
        'balance': balance,
        'partner': partner
        }

#if partner != None:
#    partner = input("partner: ")
#    data.update({'partner': partner})

with open("ser.json", "r") as f:
    ser = json.load(f)
    entry = ser['user']

for item in entry:
    if item['id'] == uid:
        if partner=='t':
            entry.remove(item)
        else:
            Partner = item['partner']
            User = item['name']
            ID = item['id']
            Balance = item['balance']
            if balance != Balance:
                Balance = balance
#            if partner != Partner:
#                Partner = partner
            if name != User:
                User = name
            item['name'] = str(User)
            item['id'] = int(ID)
            item['balance'] = int(Balance)
            item['partner'] = Partner
        break
else:
    item = None
    with open("ser.json", "w") as f:
            entry.append(data)    
            o = json.dumps(ser, indent=2)
            f.write(o)

try:
    Balance
except:
    Balance = balance
finally:
    with open("ser.json", "w") as f:
        o = json.dumps(ser, indent=2)
        f.write(o)
    print(f"You got {Balance} credits")


#if name in entry:
#    pass
#else:
#    with open("serT.json", "w") as f:
#       entry.append(data)    
#       o = json.dumps(ser, indent=2)
#       f.write(o)



#with open("ser.json", "r") as f:
#    users = json.load(f)
#if name in users:
#    print("True")
#else:
#    users.update([ ('name', name) , ('id', uid) , ('balance', balance) , ('marriage', marriage)])
#    print(users)
#with open("serT.json", "w") as f:
#    output = json.dumps(users, indent=2)
#    f.write(output)























#name = input("name: ")
#idnumber = input("id: ")
#creditsV = input("credits: ")
#marriage = input("marriage: ")
#
#class User:
#    def __init__(self, uid, name, balance, marriage):
#        self.uid = uid
#        self.name = name
#        self.balance = balance
#        self.marriage_status = marriage['status']
#        self.marriage_name = marriage['name']
#
#    @classmethod
#    def from_json(cls, json_string):
#        json_dict = json.loads(json_string)
#        return cls(**json_dict)
#    
#    def __repr__(self):
#        return f'<User { self.first_name }>'


#userdata = {
#        "user": {
#            "name": name,
#            "id": idnumber,
#            "credits": creditsV,
#            "marriage": marriage
#        }
#}
#users_list = []
#with open("users/data.json", "r") as f:
#    user_data = json.loads(f.read())
#    for u in user_data:
#        users_list.append(User(**u))
#
#print(users_list)

#with open("users/data.json", "w") as f:
#    json.dump(userdata, f, indent=4)
#
#json_str = json.dumps(userdata, indent=4)
#print(json_str)
