# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from navigationByKey import NavigationByKey
class NavigationByKeyC(NavigationByKey):
    def __init__(self, name, url,foco, navegado,xpathCalc):
        '''
        Constructor
        '''
        super(NavigationByKeyC,self).__init__(name, url, foco, navegado,xpathCalc)
if __name__== '__main__':
    x= NavigationByKeyC("evento C","foco","navegado","www.google.com","xpath")
    print(x.__str__())