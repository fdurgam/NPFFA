# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false


#import ui
#import api
#import speech
#from interactionEvent.eventoAccesibility import *
class AccessibilityEventNVDA():
    def __init__(self, name,listEventInteraction,ReportLogger):
        self.name=name
        self.listEventInteraction=listEventInteraction
        self.ReportLogger=ReportLogger
        
    def getReportLogger(self):
        return self.ReportLogger
    
    def getName(self):
        return self.name
        
    def __str__(self, *args, **kwargs):
        cadena=" Evento= name: " + self.name + " datos:"+ str(self.ReportLogger)
        return cadena  
      
if __name__== '__main__':
    x=AccessibilityEventNVDA("ContentOverlooked","","parametros")
    print (x.getReportLogger())