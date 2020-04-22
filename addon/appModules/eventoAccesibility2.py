'''
Created on 18 jun. 2018

@author: fernando
'''
import datetime

def NavigationByKeyH1():
    from navigationByKeyH import NavigationByKeyH1
    return NavigationByKeyH1("NavigationByKeyH1","listevent","www.googleom")

class eventoInteraccion(object):
    
    def __init__(self, name,url):
        '''
        Constructor
        '''
        self.name=name
        self.url=url
        self.timeStamp= datetime.datetime.now()    

class NavigationByKey(eventoInteraccion):
    '''
    constructor
    '''
    def __init__(self, name, foco, navegado, url):
        '''
        Constructor
        '''
        self.foco=foco
        self.navegado=navegado
        super(NavigationByKey,self).__init__(name,url)
        
    
    def event_caret(self,obj):
        '''
        este es el evnto que deberia llamar al loger
        type parametros: valores que describen el evetno
        
        '''
        self.logger.logEven(self.name, "parameters","asynchronic")
    
    def _get_objNavegado(self):
        return self.navegado
    
    def _get_objFocus(self):
        return self.navegado
    
    def getLogger(self):
        return self.logger
    
    

        
    
        
class NavigationByKeyH(NavigationByKey):
    def __init__(self, name, listEvent, url):
        '''
        Constructor
        '''
        foco=api.getFocusObject()
        navegado=api.getNavigatorObject()
        super(NavigationByKeyH,self).__init__(name, foco, navegado, url)
        
        
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena
    
class NavigationByKeyL(NavigationByKey):
    def __init__(self, name, listEvent, url):
        '''
        Constructor
        '''
        foco=api.getFocusObject()
        navegado=api.getNavigatorObject()
        super(NavigationByKeyL,self).__init__(name, foco, navegado,url)
    

if __name__== '__main__':
   # miLogger=logger.logger("",",","","")
    eA=NavigationByKey("NavigatorByKEyH","foco","navegado","www.google.com")
    eB=NavigationByKey("NavigatorByKEyH","foco","navegado","www.google.com")
    print eA.__str__()
    print eB.__str__()
    print str(eA._get_objNavegado())
        