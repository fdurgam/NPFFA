# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import urllib
import finder
import datetime
from eventoUtilities import Submit
from accessibilityEvent import AccessibilityEventNVDA
from datetime import date
from __builtin__ import False
class Finder(finder.Finder):
    def __init__(self,name,logger,minimunSteps,maximunScrollingTime,dwallingTime,eventName):
        super(Finder,self).__init__(name)
        self.logger=logger
        self.minimunSteps=minimunSteps
        self.maximunScrollingTime=maximunScrollingTime
        self.dwallingTime=dwallingTime
        self.threatName=eventName#"FlashScrollingAccessibilityNVDA"
        self.steps=0

    def formatParams(self):
        try:
            listEvent=self.listEvent
            steps=len(self.listEvent)
            scrollingTime=str(self.listEvent[-1].timeStamp-self.listEvent[0].timeStamp)
            url=self.listEvent[0].getUrl()
            if steps>self.minimunSteps:
                xpaths="&"
                for lista in self.listEvent:
                    xpaths=xpaths + str(lista.getXpath()) + "&"
                params={"threatName":self.threatName,"url":url,"xpaths":xpaths,"time":scrollingTime,"initialTop":self.listEvent[0].getXpath(),"finalTop":self.listEvent[-1].getXpath()}
                return params
            return False
        except:
            return None
    
    def flush(self):
        try:
            params=self.formatParams()            
            self.reset()
            if params:
                eventoAccesibilidad=AccessibilityEventNVDA(self.threatName,[],params)
                self.logger.logEven(self.threatName, params)
                return eventoAccesibilidad   
        except:
            return None
    
    def CambioUrl(self,event):     
        try:
            evento=self.flush()
            self.reset()
            self.listEvent.append(event)
            
            return evento
        except:
            return None         
    
    def approbes(self, event):
        try:
            if isinstance(event,Submit):
                return self.flush()
            if len(self.listEvent)>0:
                if (event.getUrl()!=self.listEvent[-1].getUrl()):
                    return self.CambioUrl(event) 
                if((event.timeStamp)-(self.listEvent[-1].timeStamp))>self.dwallingTime:
                    return self.flush()
            self.listEvent.append(event)
        except:
            error="error approbes"
            return None        
   
if __name__== '__main__':
    from navigationByKeyH import NavigationByKeyH
    import loggers
    logger=loggers.logger()
    server=""
    puerto=""
    token=""
    logger.setListOflink("lista")
    logger.reconfigureForKobold(server,puerto,token)
    deltaTime=datetime.timedelta(0,3,33000)
    fS=Finder("F.FlashScroll",logger,3,14000,deltaTime,'FlashScrollingAccessibilityNVDA')
    event=NavigationByKeyH("nombre1","www.site1.com","","","id=1")
    import time
    print("_________________")
    print("Test Local")
    print(fS.approbes(NavigationByKeyH("nombre1","www.site1.com","","","id=1")))
    print(len(fS.listEvent))
    time.sleep(2)
    print(fS.approbes(NavigationByKeyH("nombre","www.site1.com","","","id=1.1")))
    print(len(fS.listEvent))
    time.sleep(2)
    print(fS.approbes(NavigationByKeyH("nombre","www.site1.com","","","id=1.2")))
    print(len(fS.listEvent))
    time.sleep(4)
    print(fS.approbes(NavigationByKeyH("nombre","www.site1.com","","","id=1,2")))
    print(len(fS.listEvent))
    print(fS.approbes(NavigationByKeyH("nombre","www.site2.com","","","id=3")))
    print(len(fS.listEvent))
    print(fS.approbes(NavigationByKeyH("nombre","www.site4.com","","","id=4")))
    print(len(fS.listEvent))
    print(fS.approbes(NavigationByKeyH("nombre","www.site4.com","","","id=4")))
    print(len(fS.listEvent))
    print(fS.approbes(Submit()))
    print(fS.listEvent)
    print("_________________")
    print("Test Remoto")
    print(logger.FlashScroll)
    print("lista Evetos"+str(logger.FlashScroll.listEvent))
    
   

    
 
    