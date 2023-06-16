# Module name : urlparse -> ( https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse )
from urllib.parse import urlparse, unquote, parse_qsl
# Native Module : datetime ->
from datetime import datetime
# Native Module : secrets, json ->
import secrets, json

v_uri = 'https://www.example.com/some_path?id=1&token=Zpp24w9sXJZWKYOoMDL2y2UpOTTjUXhZuKhzSQGbn00'
# Syntax Objective : Prepare URI to Handle
v_uric = urlparse( v_uri )
# Syntax Objective : Get Domain Request
v_domain = v_uric.netloc
# Syntax Objective : Remove Point and dismount Domain
n_domain = v_domain.split('.')[0]
# Syntax Objective ->  Capture native component ( query )
v_qyco = v_uric.query

# Syntax Objective -> Treat Unwanted Characters
v_chac = unquote(v_qyco)
# Syntax Objective -> Change Query String for Dictionary
v_diry = dict(parse_qsl(v_chac))

# Syntax Objective -> Capture browser session data ( id )
v_usid = int(v_diry['id'])
# Syntax Objective -> Capture browser session data ( token )
v_usto = str(v_diry['token'])

# Syntax Objective -> Open file json and data load
v_list = open('xios/dat/session.json', 'r+')
# Syntax Objective -> 
v_data = json.load(v_list)

# Syntax Objective -> Define data type for server variable
v_seid = int()
v_seto = str()

# Syntax Objective -> Make um loop for check
for i in v_data['sessions'] :

    v_seid = i.get('id')
    v_seto = i.get('token')

# Syntax Objective : Condition values inexistent 
if v_seid == 0 and v_seto == '' :

    # Systax Objective : Get time data
    v_daho = datetime.now()
    # Systax Objective : Mount time data
    n_daho = v_daho.strftime('%d/%m/%Y %H:%M')
    # Systax Objective : To generate token of 32 bytes 
    v_seke = secrets.token_urlsafe(32)
    # Systax Objective : Json based data structure
    line = { 'date' : n_daho, 'id' : v_seid + 1, 'token': v_seke, 'status' : 'open' }
    # Systax Objective : Append line of data in file
    v_data['sessions'].append(line)
    # Systax Objective : 
    v_list.seek(0)
    # Systax Objective : Storage objects in json file
    json.dump(v_data, v_list, indent = 4)

# Systax Objective : 
elif v_usid == v_seid and v_usto == v_seto :

    print(f'( id : { v_usid } -> exist, token : { v_usto } -> exist ) : Session Status -> Open')

elif v_usid != v_seid and v_usto == v_seto :

    print(f'( id : { v_usid } -> not exist, token : { v_usto } -> exist ) : Session Status -> Closed')     

elif v_usid == v_seid and v_usto != v_seto :

    print(f'( id : { v_usid } -> exist, token : { v_usto } -> not exist ) : Session Status -> Closed')

elif v_usid != v_seid and v_usto != v_seto :

    print(f'( id : { v_usid } -> exist, token : { v_usto } -> not exist ) : Session Status -> Closed')

v_list.close()