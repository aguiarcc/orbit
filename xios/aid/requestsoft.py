# Custom Module -> ResponseHeader
from xios.aid.responseheader import ResponseHeader
# Native Module : wsgiref.static -> ( https://docs.python.org/3/library/wsgiref.html#module-wsgiref.util )
from wsgiref.util import request_uri
# Native Module : urlparse -> ( https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse )
from urllib.parse import urlparse


# Systax Objective : Define Class Super -> RequestGet
class RequestSoft( ResponseHeader ):

    # Systax Objective : Define Builder Method
    def __init__( self, envs = '', resp = '' ):
        
        # Sysntax Objective : 
        self.envs = envs
        self.resp = resp

    # Sysntax Objective : Define Handle Method 
    def handle( self, envs, resp ): 

        # Syntax Objective : Get User Request
        v_uri = request_uri( envs, include_query=True )
        # Syntax Objective : Prepare URI to Handle
        v_uric = urlparse( v_uri )
        # Syntax Objective : Get Domain Request
        v_domain = v_uric.netloc
        # Syntax Objective : Remove Point and dismount Domain
        n_domain = v_domain.split('.')[0]
        # Syntax Objective : Get Path Request
        v_path = v_uric.path
        # Syntax Objective : Remove bar, dismount path
        v_array = v_path.split('/')

        # Syntax Objective : Condition ( Apis ) Request
        if n_domain == 'api' or n_domain == 'apis' or 'api' in v_array or 'apis' in v_array:

            o_send = ResponseHeader()
            o_send.ok_text( resp )

            # Syntax Objective :  Print Message in Browser
            return [str('Request Type : Api Soft').encode('utf-8')]

        # Syntax Objective : Condition ( Browser ) Request
        elif n_domain != 'api' or n_domain != 'apis' or 'api' not in v_array or 'apis' not in v_array:

            o_send = ResponseHeader()
            o_send.ok_text( resp )
            # Syntax Objective :  Print Message in Browser
            return [str('Request Type : Browser Soft').encode('utf-8')]

        else:

            o_send = ResponseHeader()
            o_send.ise_text( resp )