# Native Module : HTTPStatus -> ( https://docs.python.org/3/library/http.html#module-http )
from http import HTTPStatus


# Systax Objective : Define Class Super -> ResponseHeader
class ResponseHeader( object ):

    # Systax Objective : Define Builder Method
    def __init__( self, v_value = '', v_phrase = '', v_status = '', v_headers = '' ):

        self.v_value = v_value
        self.v_phrase = v_phrase
        self.v_status = v_status
        self.v_headers = v_headers

    # Sysntax Objective : Define Method : Status Code : INTERNAL_SERVER_ERROR : OK : FORMAT : Html
    def http_200( self, v_resp ):
        self.v_value = str( HTTPStatus.OK.value )
        self.v_phrase = str( HTTPStatus.OK.phrase )
        self.v_status = self.v_value + ' ' + self.v_phrase
        self.v_headers = [( 'Content-type', 'text/html; charset=utf-8' )]
        return( v_resp(self.v_status, self.v_headers) )
    
    # Sysntax Objective : Define Method : Status Code : UNAUTHORIZED : UNAUTHORIZED : FORMAT : Text
    def http_401( self, v_resp ):

        self.v_value = str( HTTPStatus.UNAUTHORIZED.value )
        self.v_phrase = str( HTTPStatus.UNAUTHORIZED.phrase )
        self.v_status = self.v_value + ' ' + self.v_phrase
        self.v_headers = [
            ( 'Content-type', 'text/plain; charset=utf-8' ),
            ( 'WWW-Authenticate', 'Basic realm=Private Acess' )
        ]
        v_resp(self.v_status, self.v_headers)
        return ( 'Error: 401 Unauthorized.' )

    # Sysntax Objective : Define Method : Status Code : INTERNAL_SERVER_ERROR : INTERNAL_SERVER_ERROR : FORMAT : Text
    def http_500( self, v_resp ):

        self.v_value = str( HTTPStatus.INTERNAL_SERVER_ERROR.value )
        self.v_phrase = str( HTTPStatus.INTERNAL_SERVER_ERROR.phrase )
        self.v_status = self.v_value + ' ' + self.v_phrase
        self.v_headers = [( 'Content-type', 'text/plain; charset=utf-8' )]
        v_resp(self.v_status, self.v_headers)
        return ( 'Error: 500 Internal Server Error.' )