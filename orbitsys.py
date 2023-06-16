# Native Module : wsgiref.simple_server -> https://docs.python.org/3/library/wsgiref.html#module-wsgiref
from wsgiref.simple_server import make_server
# Native Module : asynchronous I/O -> https://docs.python.org/3/library/asyncio.html#module-asyncio
import asyncio
# Custom Module : RequestSoft
from xios.aid.requestsoft import RequestSoft


class Orbitsys( RequestSoft ):

    # Syntax Objective ->  Define Builder Method
    def __init__( self, *args, **kwargs ):
        super( Orbitsys, self ).__init__( *args, **kwargs )
        ...

    # Syntax Objective : Convert function to coroutine and be able to run concurrently ( asynchronous )
    async def asgiref( self, environ, start_response ):

        # Syntax Objective : Define time for each http request
        await asyncio.sleep( 0.01 )
        # Syntax Objective : Constructs request read object
        o_soft = RequestSoft()
        # Syntax Objective : Assign environment variable to a kosmics variable
        o_soft.envs = environ
        # Syntax Objective : Assign environment variable to a kosmics variable
        o_soft.resp = start_response
        # Syntax Objective : Activate the read method
        return [str(o_soft.handle( o_soft.envs, o_soft.resp )).encode('utf-8')]

    # Systax Objective : Send the request http to event loop 
    def wsginter( self, environ, start_response ):

        # Syntax Objective : Capture the current event loop, but it doesn't exist ? asyncio will create a new event loop and set it to current.
        loop = asyncio.get_event_loop()
        # Syntax Objective : Run until it terminate the loop and trigger the coroutine ( asgiref ) which is converted into a future.
        return loop.run_until_complete( self.asgiref( environ, start_response ) )

    # Syntax Objective : Define 
    def runcode( self ):

        # Syntax Objective : start the test server and trigger the function intermediary to wsgiref
        with make_server( '', 8000, self.wsginter ) as httpd:

            # Syntax Objective : Print terminal reference :
            print(
                'Orbiting Project\n'
                'Browser Access - http://127.0.0.1:8000\n'
                'Crl+c for uris command or Crl+z for stop'
            )

            # Syntax Objective : It persists until the process ends.
            httpd.serve_forever()
            
# Syntax Objective -> Prevent code execution when importing
if __name__ == '__main__':

    # Syntax Objective : Start Class Method
    Orbitsys().runcode()