from flask import Flask
import requests
from flask_jwt import JWT, jwt_required
import json
from collections import OrderedDict



# Credentials for authorised user to generate a token for authorised API call
USER_DATA = {
    "lunatech": "devops"
}



app = Flask(__name__)
# Secret key for token
app.config['SECRET_KEY'] = 'luna-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3000000000




#Configure User to generate token
class User(object):
    '''
    User Class setup to handle JWT
    '''
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id


def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=100)


def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}

#setup JsonWeb Token
jwt = JWT(app, verify, identity)


@app.route('/countryairportsummary', methods=['GET'])
#Ensure no unauthorised access to URL
#@jwt_required()
def airports():
    try:
        val = request.args['runwayminimumto']
        country_info = requests.get("http://0.0.0.0:8080/airports?full={}".format(1), timeout=5).json()
        # print(airports_info)
    except (requests.RequestException, ValueError):
        return ValueError

    # return airports_info[0]["iso_country"]
    # return the airports in human readable format
    #decode = json.dumps(country_info)
    #sort_order = ['ident', 'iso_country', 'runways']
    #ordered = [OrderedDict(sorted(item.items(), key=lambda: item: sort_order.index(item[0]))) for items in decode]
    #ordered = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
    #                for item in decode]
    #print(type(decode))
    #a = sorted(country_info, key = lambda i: (i['ident'], i['iso_country']))                     
    #j=json.dumps(a)
    #print(type(j))
    #return decode[0]
    #print(nuke(country_info))
    print("##########################")
    #print(getValueOf('ident', country_info))
    #print(country_info)
    #return json.dumps(getValueOf('runways', country_info))
    #val = request.args['full'] MInimum default to this and 1 or 2 return
    return json.dumps(getAnotherValueOf(country_info))
    #return getValueOf('ident', country_info)


def getAnotherValueOf(L):
    r = []
    #print({ k: dict[k] for k in dict.keys() if k == 'runways'})
    for d in L:
        for key, value in d.items():
            if key in ["ident","iso_country","runways"]:
                #print({key: print(type(d[key]))})
                if isinstance(d[key], list):
                    if len(d[key]) >= 1:
                        r.append({key: len(d[key])})
                else:
                    r.append({key: d[key]})
    return r


    

if __name__ == '__main__':
    app.run(debug=True)
