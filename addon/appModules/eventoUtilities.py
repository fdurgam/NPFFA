# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from eventoInteraccion import evento
class Submit(evento):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.name='Submit'
        self.url='None'
        super(Submit,self).__init__(self.name,self.url)
    
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena
    
if __name__== '__main__':
    x= Submit()
    print(x)