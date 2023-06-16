

class SessionPage( object ) :

    # Systax Objective : Define Builder Method
    def __init__(self) -> None:
        pass

    # Sysntax Objective : Define Send Method 
    def handle( self, v_seid, v_seke ) :

        # Sysntax Objective :  Define variable for code html
        code = """
<!DOCTYPE html>
<html lang="pt-br">

    <head>

        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300&display=swap" rel="stylesheet">
        <style>body { font-family: 'Titillium Web', sans-serif; font-size: 16px; }</style>

        <title>Kosmics Orbit</title>

    </head>

    <body>
        Entering in orbit . . .
        <script>
            $(document).ready(function() {
            
                // Armazenar um valor no sessionStorage
                sessionStorage.setItem('id', """ + v_seid + """);
                sessionStorage.setItem('token', """ + v_seke + """);

            });
        </script>
        <script src="https://code.jquery.com/jquery-3.7.0.min.js" integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" crossorigin="anonymous"></script>
    </body>
</html>
        """ 
        return(code)