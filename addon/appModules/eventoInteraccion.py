# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import datetime
class evento(object):
    
    def __init__(self,name,url):
        '''
        Constructor
        '''
        self.name=name
        self.url=url
        self.timeStamp= datetime.datetime.now()
        
    def getTimeStamp(self):
        return self.timeStamp
    
    def getXpath(self):
        return None
        
    def setXpath(self,xpath):
        self.xpath=xpath
    
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena    
        
    def getUrl(self):
        return self.url
    
    