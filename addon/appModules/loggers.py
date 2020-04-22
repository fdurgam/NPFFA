import httplib,urllib
import json
import os
from datetime import datetime
import datetime
from __builtin__ import True
import dispatcher3
import time
import FlashScrollKey
import NavListAndLink
class config(object):
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

class logger(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        conf=config('conf.ini')
        self.server=conf.server
        self.port=conf.port
        self.api=conf.api
        self.eventos=[]
        self.url=None
        self.token=""
        self.dispacher=dispatcher3.dispatcher()
        self.finders=[]
        deltaTime=datetime.timedelta(0,10,33000)
        self.FlashScroll=FlashScrollKey.Finder("F.FlashScroll",self,2,16990,deltaTime,'FlashScrollingAccessibilityNVDA')
        self.finders.append(self.FlashScroll)
        deltaTime=datetime.timedelta(0,10,96000)
        self.LinkAndList=NavListAndLink.Finder("F.LinkAndList",self,2,24540,deltaTime,2,'NavigationBetweenListsAndLink')
        self.finders.append(self.LinkAndList)
        
    def reconfigure(self,server,port,api,token):
        try:
            self.server=server
            self.port=port
            self.api=api
            self.token=token
            return True
        except: 
            return None
    
    def reconfigureForKobold(self,server,port,token):
        try:
            self.server=server
            self.port=port      
            self.token=token
            return True
        except: 
            return None
        
    def logEven(self, threatName, params):      
        try:
            self.send(threatName, params, False)
        except:
            error="error logEven" 
           
    def send(self, threatName, params, asynchronic):
        try:
            parameters={"token":self.token, "threat":threatName,"timestamp":datetime.datetime.now()}
            params["token"]=self.token
            params["threat"]=threatName
            params["timestamp"]=int(round(time.time()*1000))
            params["url"]=self.url
            params=urllib.urlencode(params)      
            headers= {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
            conn=httplib.HTTPConnection(self.server+":"+self.port)
            request=conn.request("POST","/Threats",params,headers)
            response=conn.getresponse()
        except:
            error="error send" 
        
    def newEvent(self,direccion,gesture,foco,navegado,xpath,url,children):
        try:
            
            inputkey=gesture.mainKeyName
            evento=self.dispacher.event(inputkey,foco,navegado,xpath,url,children)
            if evento:              
                self.finderEvent(self.finders,evento)
            self.url=url;
        except: 
            error='error new event'
            
    def setListOflink(self,lista):
        lista1=lista
        self.LinkAndList.setListOflink(lista)
    
    def finderEvent(self,finders,Event):
        try:
            for finder in self.finders:     
                finder.approbes(Event)            
        except:
            error="Error finder event"
    
    def newEventSubmit(self):
        try:  
            evento=self.dispacher.eventSubmit()
            if evento:
                self.finderEvent(self.finders,evento)
            return evento
        except: 
            error='error newEventSubmit'
            return None
 
class newGesture(object):
    def __init__(self, gesto):
        self.mainKeyName=gesto

class navegado(object):
    def __init__(self, children):
        self.children=children

if __name__ == '__main__':
    log=logger()
    
    deltaTime=datetime.timedelta(0,3,20300)
    import FlashScrollKey
    import NavListAndLink
    
   
    #log.agragarFinder(FlashScrollKey.Finder("F.FlashScroll",log,3,14000,deltaTime,'FlashScrollingAccessibilityNVDA'))  
    #log.agragarFinder(NavListAndLink.Finder("F.LinkAndList",log,2,14000,30000,3,'NavigationBetweenListsAndLink'))
    
    
    #Genera los Eventos
    log.reconfigure("192.168.1.110","8080","/api/post3.php","7c0863c3-e05b-0d00-a2b2-193302d0013a")
    log.logEven("ff",params={"threatName":"4d620a19-fe5c-0d00-ab8e-fb1f0d38c2fb","url":1,"xpaths":1,"time":122,"initialTop":1,"finalTop":1,"token":"4d620a19-fe5c-0d00-ab8e-fb1f0d38c2fb"});
    log.newEvent("next",newGesture('h'),"foco",navegado(5),"id=21",'www.google.com.ar',3)
    print(len(log.finders[0].listEvent))
    
    log.newEvent("next",newGesture('l'),"foco",navegado(6),"id=22",'www.google.com.ar',5)
    print(len(log.finders[0].listEvent))
    
    log.newEvent("next",newGesture('l'),"foco",navegado(8),"id=23",'www.google.com.ar',6)
    print(len(log.finders[0].listEvent))
    
    log.newEvent("next",newGesture('l'),"foco",navegado(9),"id=24",'www.google.com.ar',5)
    print(len(log.finders[0].listEvent))
    #finder=log.finders[0]
    #evento=log.newEvent("next",newGesture('l'),"foco","navegado","id=23",'www.google.com.ar')
    print('por enviar')
    
    log.newEventSubmit()
    #finder.approbes(log.newEvent("next",newGesture('l'),"foco","navegado","id=23",'www.google.com.ar'))
    #print(finder.formatParams())
    #print(finder.logger.logEven('',finder.formatParams()))
    log.newEvent("next",newGesture('l'),"foco",navegado(9),"id=25",'www.google.com.ar',5)
    print(len(log.finders[0].listEvent))
    log.newEvent("next",newGesture('l'),"foco",navegado(9),"id=26",'www.google.com.ar',8)
    print(len(log.finders[0].listEvent))