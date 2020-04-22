# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from eventoInteraccion import evento
class NavigationByKey(evento):
    '''
    constructor
    '''
    def __init__(self, name, url, foco, navegado, xpath):
        '''
        Constructor
        '''
        self.foco=foco
        self.navegado=navegado
        self.xpath=xpath
        super(NavigationByKey,self).__init__(name,url)
    
    def _get_objNavegado(self):
        return self.navegado
    
    def _get_objFocus(self):
        return self.foco
    
    def _setFoco(self,foco):
        self.foco=foco
    
    def _setNavegado(self,navegado):
        self.navegado=navegado
        
    def getChildCount(self):
        return 0
    
    def getXpath(self):
        return self.xpath
   
if __name__== '__main__':
    x= NavigationByKey("evento1","foco","navegado","www.google.com","xpath")
    print(x.getXpath())
    print(x.__str__())