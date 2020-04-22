# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
#

from eventoInteraccion import evento
from navigationByKeyH import NavigationByKeyH
from navigationByKeyL import NavigationByKeyL
from navigationByKeyI import NavigationByKeyI
from navigationByKeyT import NavigationByKeyT
from navigationByKeyK import NavigationByKeyK
from navigationByKeyS import NavigationByKeyS
from navigationByKeyM import NavigationByKeyM
from navigationByKeyG import NavigationByKeyG
from navigationByKeyD import NavigationByKeyD
from navigationByKeyO import NavigationByKeyO
from navigationByKeyN import NavigationByKeyN
from navigationByKeyF import NavigationByKeyF
from navigationByKeyU import NavigationByKeyU
from navigationByKeyV import NavigationByKeyV
from navigationByKeyE import NavigationByKeyE
from navigationByKeyB import NavigationByKeyB
from navigationByKeyX import NavigationByKeyX
from navigationByKeyC import NavigationByKeyC
from navigationByKeyR import NavigationByKeyR
from navigationByKeyQ import NavigationByKeyQ
from eventoUtilities import Submit


class dispatcher():
	def __init__(self):
		pass
	
	def eventSubmit(self):
		return Submit()
	
	def event(self,inputKey,foco,navegado,xpath,url,children):
		try: 
			
			if inputKey=="h":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado,xpath)
			if inputKey=="l":
				eventI= NavigationByKeyL("NavigationByKeyL", url, foco, navegado,xpath,children)			
			if inputKey=="i":
				eventI= NavigationByKeyI("NavigationByKeyI", url, foco, navegado,xpath)
			if inputKey=="t":
				eventI= NavigationByKeyT("NavigationByKeyt", url, foco, navegado,xpath)
			if inputKey=="k":
				eventI= NavigationByKeyK("NavigationByKeyk", url, foco, navegado,xpath)
			if inputKey=="n":
				eventI= NavigationByKeyN("NavigationByKeyN", url, foco, navegado,xpath)
			if inputKey=="f":
				eventI= NavigationByKeyF("NavigationByKeyF", url, foco, navegado,xpath)
			if inputKey=="u":
				eventI= NavigationByKeyU("NavigationByKeyU", url, foco, navegado,xpath)
			if inputKey=="v":
				eventI= NavigationByKeyV("NavigationByKeyV", url, foco, navegado,xpath)
			if inputKey=="e":
				eventI= NavigationByKeyE("NavigationByKeyE", url, foco, navegado,xpath)
			if inputKey=="b":
				eventI= NavigationByKeyB("NavigationByKeyB", url, foco, navegado,xpath)
			if inputKey=="x":
				eventI= NavigationByKeyX("NavigationByKeyX", url, foco, navegado,xpath)
			if inputKey=="c":
				eventI= NavigationByKeyC("NavigationByKeyC", url, foco, navegado,xpath)
			if inputKey=="r":
				eventI= NavigationByKeyR("NavigationByKeyC", url, foco, navegado,xpath)
			if inputKey=="q":
				eventI= NavigationByKeyQ("NavigationByKeyQ", url, foco, navegado,xpath)
			if inputKey=="s":
				eventI= NavigationByKeyS("NavigationByKeyS", url, foco, navegado,xpath)
			if inputKey=="m":
				eventI= NavigationByKeyM("NavigationByKeyM", url, foco, navegado,xpath)
			if inputKey=="g":
				eventI= NavigationByKeyG("NavigationByKeyG", url, foco, navegado,xpath)
			if inputKey=="d":
				eventI= NavigationByKeyD("NavigationByKeyD", url, foco, navegado,xpath)
			if inputKey=="o":
				eventI= NavigationByKeyO("NavigationByKeyO", url, foco, navegado,xpath)
			if inputKey=="1":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpath)
			if inputKey=="2":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpath)
			if inputKey=="3":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpath)
			if inputKey=="4":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpath)
			if inputKey=="5":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpath)
			if inputKey=="6":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpath)
			
			return eventI
		except:
			error="Error al crear el evento de interaccion"

if __name__ == '__main__':	
		disp=dispatcher()
		resultado=disp.event('h',"foco","navegado","xpath","url",0)
		print(resultado)
		resultado=disp.event('l',"foco","navegado","xpath","url",3)
		print(resultado)
		resultado=disp.event('l',"foco","navegado","xpath","url",3)
		print(resultado)
		resultado=disp.event('l',"foco","navegado","xpath","url",3)
		print(resultado)
		resultado=disp.event('l',"foco","navegado","xpath","url",3)
		print(resultado)
		resultado=disp.event('m',"foco","navegado","xpath","url",3)
		print(resultado)
		resultado=disp.event('g',"foco","navegado","xpath","url",3)
		print(resultado)
		resultado=disp.event('d',"foco","navegado","xpath","url",3)
		print(resultado)
		resultado=disp.event('o',"foco","navegado","xpath","url",3)
		print(resultado)
		resultado=disp.eventSubmit()
		print (resultado)
			
