import hashlib
from urllib.parse import urlparse, parse_qs

import pyotp
import requests
from sqlalchemy import text

from gettoken.additionalfunction import createengine,gettoday
from globalvariable import readContext
from sid import getsid3


def getfreshtoken():
    try:
        APIKEY = readContext().getVariable('APIKEY')
        secretKey = readContext().getVariable('SECRET_KEY')
        totp_key = readContext().getVariable('TOTP')
        password = readContext().getVariable('PASSWORD')
        userid = readContext().getVariable('USER')
        SID = getsid3()
        passwordEncrpted = hashlib.sha256(password.encode()).hexdigest()
        ses = requests.Session()
        url2 = 'https://authapi.flattrade.in/ftauth'
        payload = {"UserName": userid, "Password": passwordEncrpted, "PAN_DOB": pyotp.TOTP(totp_key).now(), "App": "","ClientID": "", "Key": "", "APIKey": APIKEY, "Sid": SID}
        print(payload)
        res2 = ses.post(url2, json=payload)
        reqcodeRes = res2.json()
        print(reqcodeRes)
        parsed = urlparse(reqcodeRes['RedirectURL'])
        print(parsed)
        reqCode = parse_qs(parsed.query)['code'][0]
        api_secret = APIKEY + reqCode + secretKey
        api_secret = hashlib.sha256(api_secret.encode()).hexdigest()
        payload = {"api_key": APIKEY, "request_code": reqCode, "api_secret": api_secret}
        url3 = 'https://authapi.flattrade.in/trade/apitoken'
        res3 = ses.post(url3, json=payload)
        token = res3.json()['token']
        return token
    except:
        print("There is some error while getting Fresh token")


def gettokenfromdatabase():
    try:
        engine  =  createengine()
        today = str(gettoday())
        query = f"select * from FlatTrade.Token WHERE DATE ='{today}'"
        # print(query)
        conn = engine.connect()
        result = conn.execute(text(query))
        # print(list(result.keys()))
        conn.close()
        res = result.all()
        if (len(res) > 1): print(f"There is issue with counts more than 1 count={len(res)}")
        for result in res:
            return result.Token

    except Exception as ex:
        print("There is some issue while getting the token from data base")
        raise ex

def tokenController():
    databasetoken = gettokenfromdatabase()
    if databasetoken is None:
        print("Data Base token is None getting Token from fresh")
        freshtoken =  getfreshtoken()
        insertnewtoken(freshtoken)
        return freshtoken
    else:
        return databasetoken

def insertnewtoken(newtoken :str):
    try:
        if newtoken == None:
            raise RuntimeWarning("The insert token is None")
            return None
        engine  =  createengine()
        today = str(gettoday())
        query = f"INSERT INTO FlatTrade.Token (Token,`Date`) values('{newtoken}','{today}')"
        print(query)
        conn = engine.connect()
        result = conn.execute(text(
            "INSERT INTO FlatTrade.Token (Token,Date) values(:Token,:Date)"),
            [{"Token": newtoken, "Date": today}]
        )
        # print(result.inserted_primary_key)
        conn.commit()
    except Exception as ex:
        print("There is some issue while inserting the new token")
        raise ex


if __name__ == '__main__':
    print(tokenController())