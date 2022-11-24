import paths as pp
import json


def getData():
    with open(pp.compData, 'r') as compData:
        return json.load(compData)


def updateData(data):
    db = getData()
    for i, j in data.items():
        db[i] = j

    with open(pp.compData, 'w') as compData:
        json.dump(db, compData, indent=4)
        print('compDat.json update complete')


# updateData({
#     "Deviyani": {
#         "email": "deviyani492@gmail.com",
#         "address": "devi address"
#     },
#     "Pradeep": {
#         "email": "pradeep492@gmail.com",
#         "address": "pradeep address"
#     }
# })


data = {
    'Deviyani': {
        'email': 'deviyani492@gmail.com',
        'address': 'Some address'
    },
    'Yogesh': {
        'email': 'yogeshyoge739@gmail.com',
        'address': 'Some address'
    },
    'Barath': {
        'email': 'aravindkbarath@gmail.com',
        'address': 'Some address'
    },
    'Vijay': {
        'email': 'vijayvenkatesh2212@gmail.com',
        'address': 'Some address'
    },
}
