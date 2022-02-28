import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
file = open('sample.json')
f = file.read()
data = json.loads(f)
for i in range(len(data['imdata'])):
    if len(data['imdata'][i]['l1PhysIf']['attributes']['dn']) == 42:
        print(f"{data['imdata'][i]['l1PhysIf']['attributes']['dn']}                               {data['imdata'][i]['l1PhysIf']['attributes']['fecMode']}  {data['imdata'][i]['l1PhysIf']['attributes']['mtu']}")
    else:
        print(f"{data['imdata'][i]['l1PhysIf']['attributes']['dn']}                                {data['imdata'][i]['l1PhysIf']['attributes']['fecMode']}  {data['imdata'][i]['l1PhysIf']['attributes']['mtu']}")
