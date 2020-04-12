import json
balance = 5000
marriage = False

name = input("name: ")
uid = int(input("id: "))
#balance = int(input("balance: "))
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
