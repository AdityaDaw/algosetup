from globalvariable import readContext
from gettoken import tokenController

def apiSessionCreator():
    password = readContext().getVariable("PASSWORD")
    userid = readContext().getVariable("USER")
    token = tokenController()

    from NorenRestApiPy.NorenApi import NorenApi

    class FlatTradeApiPy(NorenApi):
        def __init__(self):
            NorenApi.__init__(self, host='https://piconnect.flattrade.in/PiConnectTP/',
                              websocket='wss://piconnect.flattrade.in/PiConnectWSTp/',
                              eodhost='https://web.flattrade.in/chartApi/getdata/')
    api = FlatTradeApiPy()

    ret = api.set_session(userid=userid, password=password, usertoken=token)

    if ret is not None:
        return api
    else:
        print("Return is None while setting the session fail")
        exit(1)