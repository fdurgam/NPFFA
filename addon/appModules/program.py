import httplib,urllib
import json
import os
from datetime import datetime
import datetime
from __builtin__ import True
#import ui
import dispatcher3

import loggers

from loggers import config
class Program(object):
    
    def __init__(self, file):
        directorio=os.path.dirname(os.path.abspath(__file__))
        file=directorio+"/conf.ini"
        file=open(file)
        lines=file.readlines()
        for line in lines:
            valor=line.split()
            if valor[0]=="server":
                self.server=valor[2]
            if valor[0]=="port":
                self.port=valor[2]
            if valor[0]=="api":
                self.api=valor[2]
        
        
    def getserver():
        return self.server

    def getport():
        return self.port

    def getapi():
        return self.api

class newGesture(object):
    def __init__(self, gesto):
        self.mainKeyName=gesto
        
    
    
class navegado(object):
    def __init__(self, children):
        self.children=children
        
    def getChildCount(self):
        return self.children
    


if __name__ == '__main__':
    #Crea el loggeer
   
    
    import loggers
    logger=loggers.logger()
    server="192.168.1.110"
    puerto="8080"
    token="201857ef-f75f-0d00-afc2-4aa0069817e9"
    logger.setListOflink("lista")
    logger.reconfigureForKobold(server,puerto,token)
    #Configura los finders
    deltaTime=datetime.timedelta(0,3,20300)
   
    #Genera los Eventos
   
    import time
    
    logger.newEvent("next",newGesture('l'),"foco",navegado(5),"id=21",'www.google.com.ar',6)
    print("lista FlashScroll= "+str(len(logger.finders[0].listEvent)))
    print("lista LinkAndList= "+str(len(logger.finders[1].listEvent)))
    time.sleep(2)
    logger.newEvent("next",newGesture('l'),"foco",navegado(6),"id=22",'www.google.com.ar',5)
    print("lista 0= "+str(len(logger.finders[0].listEvent)))
    print("lista 1= "+str(len(logger.finders[1].listEvent)))
    
    logger.newEvent("next",newGesture('l'),"foco",navegado(8),"id=23",'www.google.com.ar',6)
    print("lista 0= "+str(len(logger.finders[0].listEvent)))
    print("lista 1= "+str(len(logger.finders[1].listEvent)))
    
    logger.newEvent("next",newGesture('l'),"foco",navegado(9),"id=24",'www.google.com.ar',5)
    
    print("lista 0= "+str(len(logger.finders[0].listEvent)))
    print("lista 1= "+str(len(logger.finders[1].listEvent)))
    #finder=log.finders[0]
    #evento=log.newEvent("next",newGesture('l'),"foco","navegado","id=23",'www.google.com.ar')
   
   
    logger.newEventSubmit()
    #finder.approbes(log.newEvent("next",newGesture('l'),"foco","navegado","id=23",'www.google.com.ar'))
    #print(finder.formatParams())
    #print(finder.logger.logEven('',finder.formatParams()))
    logger.newEvent("next",newGesture('l'),"foco",navegado(9),"id=25",'www.google.com.ar',5)
    print("lista 0= "+str(len(logger.finders[0].listEvent)))
    print("lista 1= "+str(len(logger.finders[1].listEvent)))
    logger.newEvent("next",newGesture('l'),"foco",navegado(9),"id=26",'www.google.com.ar',8)
    print("lista 0= "+str(len(logger.finders[0].listEvent)))
    print("lista 1= "+str(len(logger.finders[1].listEvent)))
    import time
    millis = int(round(time.time()*1000))
    print millis



   
   