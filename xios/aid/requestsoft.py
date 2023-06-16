# Custom Module -> ResponseHeader
from xios.aid.responseheader import ResponseHeader
# Custom Module ->  Session Manager
from xios.aid.sessionmanager import SessionManager
# Native Module : wsgiref.static -> ( https://docs.python.org/3/library/wsgiref.html#module-wsgiref.util )
from wsgiref.util import request_uri
# Native Module : urlparse -> ( https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse )
from urllib.parse import urlparse


# Systax Objective : Define Class Super -> RequestGet
class RequestSoft( ResponseHeader, SessionManager ):

    # Systax Objective : Define Builder Method
    def __init__( self, v_envs = '', v_resp = '' ):
        
        # Sysntax Objective : 
        self.v_envs = v_envs
        self.v_resp = v_resp

    # Sysntax Objective : Define Handle Method 
    def handle( self, v_envs, v_resp ): 

        # Syntax Objective : Get User Request
        v_uri = request_uri( v_envs, include_query=True )
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
        # Syntax Objective ->  Capture native component ( query )
        v_qyco = v_uric.query

        # Syntax Objective : Condition ( Apis ) Request
        if n_domain == 'api' or n_domain == 'apis' or 'api' in v_array or 'apis' in v_array:

            # Syntax Objective : Instance the class e build object
            o_send = ResponseHeader()
            # Syntax Objective :  Send parameter for trigger response http
            o_send.ok_text( v_resp )
            # Syntax Objective :  Print Message in Browser
            return ('Request Type : Api Soft')

        # Syntax Objective : Condition ( Browser ) Request
        elif n_domain != 'api' or n_domain != 'apis' or 'api' not in v_array or 'apis' not in v_array:

            # Syntax Objective : Instance the class e build object
            o_send = ResponseHeader()
            # Syntax Objective :  Send parameter for trigger response http
            o_send.ok_html( v_resp )

            # Syntax Objective : Instance the class e build object
            o_instance = SessionManager()
            # Syntax Objective :  Send parameter for trigger response http
            return (o_instance.handle( v_envs ))

        else:

            # Syntax Objective : Instance the class e build object
            o_send = ResponseHeader()
            # Syntax Objective :  Send parameter for trigger response http
            o_send.ise_text( v_resp )