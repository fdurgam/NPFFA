# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import urllib
import finder
from navigationByKeyL import NavigationByKeyL
from eventoUtilities import Submit
from datetime import date
from accessibilityEvent import AccessibilityEventNVDA
class Finder(finder.Finder):
    def __init__(self, name,logger,minimunSteps,maximunScrollingTime,dwallingTime,minimunChildren,eventName):
        self.minimunSteps=minimunSteps
        self.maximunScrollingTime=maximunScrollingTime
        self.dwallingTime=dwallingTime
        self.minimunChildren=minimunChildren
        self.threatName=eventName#"NavigationBetweenListsAndLink"
        self.logger=logger
        self.eventName=eventName
        self.lista=[]
        super(Finder,self).__init__(name)
       
    def flush(self):
        try:
            params=self.formatParams()
            self.reset()
            if params:
                self.logger.logEven(self.threatName, params)
                eventoAccesibilidad=AccessibilityEventNVDA(self.threatName,[],params) 
                return eventoAccesibilidad
        except:
            return None
                
    def formatParams(self):
        try:
            if len(self.listEvent)>self.minimunSteps:
                list=[]
                url=self.listEvent[0].getUrl()
                xpaths="&"
                for lista in self.listEvent:      
                    xpaths=xpaths + str(lista.getXpath()) + "&"           
                    list.append(str(lista.getChildCount()))       
                params={"threatName":self.threatName,"url":url,"xpaths":xpaths,"countElement":list,"initialTop":self.listEvent[0].getXpath(),"finalTop":self.listEvent[-1].getXpath()}
                return params
            return False
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
        
    def setListOflink(self, cadena):
        try:   
            lista=cadena.split(',')     
            self.lista=lista 
        except:
            error="erro set List Of link"
            return None
        
    def isNotAllNodeLink(self,id):
        try:
            stringID=str(id)
            if stringID not in self.lista:
                return True
            return False
        except:
            error=" is Not All Node Link"
            return None
    
    def approbes(self, event):
        try:
            if isinstance(event,Submit):
                return self.flush()
            if(self.isNotAllNodeLink(event.getXpath())):
                return self.flush()
            if len(self.listEvent)>0:
                if (event.getUrl()!=self.listEvent[-1].getUrl()):
                    return self.CambioUrl(event)
                if((event.timeStamp)-(self.listEvent[-1].timeStamp))>self.dwallingTime:
                    return self.flush()
            if isinstance(event,NavigationByKeyL):
                self.listEvent.append(event)
            else:
                return self.flush()
                  
        except:
            error="error approbes"
            return None
            


if __name__== '__main__':
    import datetime
    deltaTime=datetime.timedelta(0,3,00000)
    from navigationByKeyL import NavigationByKeyL
    FN=Finder("F.LinkAndList",'log',2,14000,deltaTime,3,'NavigationBetweenListsAndLink')
    print(FN)
    listaid="id=3,id=4,id=5,/html/body/div[6]/div/div[10]/div[3]/div/div[2]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div/div[3]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div/div[4]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div[3]/div/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div[3]/div[2]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div[3]/div[3]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div[3]/div[4]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div[3]/div[5]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div[3]/div[6]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div[3]/div[7]/div/div[2]/div[10]/ul,/html/body/div[6]/div/div[10]/div[3]/div[3]/div[8]/div/div[2]/div[10]/ul"
    FN.setListOflink(listaid)
    id="id=3";
    import time
    
    print(FN.isNotAllNodeLink(id))
    print(FN.lista)
    
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","foco","navegado","id=3",6)))
    print(len(FN.listEvent))
    time.sleep(2)
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","","","id=4",5)))
    print(len(FN.listEvent))
    time.sleep(1)
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","","","id=5",7)))
    print(len(FN.listEvent))
    time.sleep(4)
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","","","id=3",8)))
    print(len(FN.listEvent))
    time.sleep(1)
    print(FN.approbes(Submit()))
    print(len(FN.listEvent))
    time.sleep(1)
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","","","id=4",5)))
    print(len(FN.listEvent))
    time.sleep(1)
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","","","id=5",7)))
    print(len(FN.listEvent))
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","","","id=3",8)))
    print(len(FN.listEvent))
    time.sleep(1)
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.google2.com","","","id=3",8)))
    print(len(FN.listEvent))
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","","","id=5",7)))
    print(len(FN.listEvent))
    time.sleep(1)
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.site1.com","","","id=3",8)))
    print(len(FN.listEvent))
    time.sleep(4)
    print(FN.approbes(NavigationByKeyL("NavigationByKeyL","www.google2.com","","","id=3",8)))
    print(len(FN.listEvent))

        