from datetime import datetime

from sqlalchemy import engine

from globalvariable import readContext




def createengine():
    url = readContext().getVariable("DATABASEURL")
    return engine.create_engine(url)

def gettoday():
    return datetime.today().date()