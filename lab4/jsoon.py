import json
with open('sample-data.json','r') as zhakeee:
    readd=zhakeee.read()
readd=json.loads(readd)#loads-загружает
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in readd['imdata']: 
    print(i['l1PhysIf']["attributes"]['dn'], "                            ",  i['l1PhysIf']["attributes"]['speed']," ", i['l1PhysIf']["attributes"]['mtu'])
