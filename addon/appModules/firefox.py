# NVDA Keyboard Event Capture for Mozilla Firefox
#This fil is covered by the GNU General Public License.
#See the file COPYING.txt for more details.cc
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false

from nvdaBuiltin.appModules import firefox
import addonHandler
import globalCommands
import controlTypes
import api
import ui
import datetime
import browseMode
from NVDAObjects import NVDAObject
import loggers
addonHandler.initTranslation()

class AppModule(firefox.AppModule):	
	url=""
	logger=loggers.logger()
	def event_gainFocus(self, obj, nextHandler):
		try:
			if  str(obj.role)=="52":							
				self.url=self.buscarbyid(obj,"id", "url")
				self.server=self.buscarbyid(obj,"id", "server")
				self.puerto=self.buscarbyid(obj,"id", "puerto")
				self.api=self.buscarbyid(obj,"id", "api")
				self.token=self.buscarbyid(obj,"id", "token")
				self.logger.reconfigureForKobold(self.server,self.puerto,self.token)
				lista=self.buscarbyid(obj,"id", "lista")				
				self.logger.setListOflink(lista)
			nextHandler()
		except:
			error="Error event_gainFocus"
		
	def buscarbyid(self,obj,id,value):
		try:
			obj1 = self.searchAmongTheChildren(id,value,obj)
			if not obj1:
				return
			return obj1
		except:
			error="buscarbyid"
						
	def searchAmongTheChildren(self, id,value,obj):
		try:
			if not obj:
				return(None)
			obj=obj.firstChild
			if id in obj.IA2Attributes.keys():
				if obj.IA2Attributes[id] == value:
					data=(str(obj.firstChild.IA2Attributes[id]))
					return data
			while obj:
				if id in obj.IA2Attributes.keys():
					if obj.IA2Attributes[id] == value:
						data=str(obj.firstChild.IA2Attributes[id])
						break
				obj = obj.next
			return data
		except:
			error="error searchAmongTheChildren"
			

	def event_typedCharacter(self,obj,nextHandler):
		try:
			self.logger.newEventSubmit()
			nextHandler()										
		except:
			error="error event_typedCharacter"

	def event_valueChange(self, obj, nextHandler):
		try:
			self.logger.newEventSubmit()
			nextHandler()		
 		except:
			error="error  event_valueChange"
			
			
	
	def event_stateChange(self, obj, nextHandler):
		try:
			self.logger.newEventSubmit()
			nextHandler()				
		except:
			error="error  event_stateChange"			

	def script_dispatchEventPrevious(self, gesture):
		try:	
			if not self.objNav():
				gesture.send()	
			else:
				if self.modo():
					gesture.send()
				else:
					if (not self.navegar('previous',gesture)):
						fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
						shift=True
						obj=api.getNavigatorObject()
						navegado=api.getNavigatorObject()
						childrens=0		
						if gesture.mainKeyName=='l':
         					 while not obj.role==controlTypes.ROLE_LIST:
         					 	obj=obj.parent
 				 			childrens=obj.childCount
 				 		xpath=str(obj.IA2Attributes["id"])
						self.logger.newEvent("previous",gesture,'foco',navegado,xpath,self.url,childrens)
		except:
			error="error script_dispatchEventPrevious"
	
	def script_dispatchEventNext(self, gesture):
		try:
			
			if not self.objNav():
				gesture.send()	
			else:
				if self.modo():
					gesture.send()
				else:				
					if (not self.navegar('next',gesture)):
						fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
						shift=True
						obj=api.getNavigatorObject()
						navegado=api.getNavigatorObject()
						childrens=0
						if gesture.mainKeyName=='l':
         					 while not obj.role==controlTypes.ROLE_LIST:
         					 	obj=obj.parent
         					childrens=obj.childCount
 				 		xpath=str(obj.IA2Attributes["id"])
						self.logger.newEvent("next",gesture,'foco',navegado,xpath,self.url,childrens)
 		except:
 			error="error script_dispatchEventNext"
	
	def modo(self):
		try:
			focus = api.getFocusObject()
			vbuf = focus.treeInterceptor
			if not vbuf:
				for obj in itertools.chain((api.getFocusObject(),), reversed(api.getFocusAncestors())):
					try:
						obj.treeInterceptorClass
					except:
						continue
					break
				else:
					return
				ti = treeInterceptorHandler.update(obj, force=True)
				if not ti:
					return
				if focus in ti:
					focus.treeInterceptor = ti
					if isinstance(ti,browseMode.BrowseModeTreeInterceptor) and not ti.passThrough:
						browseMode.reportPassThrough(ti,False)
				return
		
			if not isinstance(vbuf, browseMode.BrowseModeTreeInterceptor):
				return
			if vbuf.passThrough:
				return True
			else:
				return False		
		except:
			error="error modo"
	
	def ignorar_gesto(self, gesto):
 		api.getFocusObject().treeInterceptor.script_collapseOrExpandControl(gesto)
 	
 	def navegar(self,direction,gesture):
 		try: 
 		 	obj=api.getNavigatorObject().treeInterceptor
 		 	previo=api.getNavigatorObject()
		 	inputGesture=gesture.mainKeyName
			if inputGesture=="h":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading(obj,gesture)
			if inputGesture=="l":
				if direction=="next":		
					browseMode.BrowseModeTreeInterceptor.script_nextList(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousList(obj,gesture)
			if inputGesture=="i":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextListItem(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousListItem(obj,gesture)
			if inputGesture=="t":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextTable(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousTable(obj,gesture)
			if inputGesture=="k":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextLink(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousLink(obj,gesture)
			if inputGesture=="n":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextNotLinkBlock(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousNotLinkBlock(obj,gesture)
			if inputGesture=="f":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextFormField(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previoustFormField(obj,gesture)
			if inputGesture=="u":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextUnvisitedLink(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousUnvisitedLink(obj,gesture)
			if inputGesture=="v":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextVisitedLink(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousVisitedLink(obj,gesture)
			if inputGesture=="e":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextEdit(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousEdit(obj,gesture)
			if inputGesture=="b":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextButton(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousButton(obj,gesture)
			if inputGesture=="x":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextCheckBox(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousCheckBox(obj,gesture)
			if inputGesture=="c":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextComboBox(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousComboBox(obj,gesture)
			if inputGesture=="r":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextRadioButton(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousRadioButton(obj,gesture)
			if inputGesture=="q":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextBlockQuote(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousBlockQuote(obj,gesture)
			if inputGesture=="s":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextSeparator(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousSeparator(obj,gesture)
			if inputGesture=="m":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextFrame(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousFrame(obj,gesture)
			if inputGesture=="g":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextGraphic(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousGraphic(obj,gesture)
			if inputGesture=="d":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextLandmark(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousLandmark(obj,gesture)
			if inputGesture=="o":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextEmbeddedObject(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousEmbeddedObject(obj,gesture)
			if inputGesture=="1":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading1(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading1(obj,gesture)
			if inputGesture=="2":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading2(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading2(obj,gesture)
			if inputGesture=="3":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading3(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading3(obj,gesture)
			if inputGesture=="4":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading4(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading4(obj,gesture)
			if inputGesture=="5":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading5(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading5(obj,gesture)
			if inputGesture=="6":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading6(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading6(obj,gesture)
			if previo==api.getNavigatorObject():		
				return True
			else:
				return False
		except:
			error="error navegar"	
			
	def objNav(self):
		try:
			obj=api.getFocusObject()
			while not obj.role==controlTypes.ROLE_DOCUMENT:
				obj=obj.parent
			return True	
		except:
			return False
		
	__gestures = {
		"kb:h": "dispatchEventNext",
		"kb:shift+h": "dispatchEventPrevious",
		"kb:l": "dispatchEventNext",
		"kb:shift+l": "dispatchEventPrevious",
		"kb:i": "dispatchEventNext",
		"kb:shift+i": "dispatchEventPrevious",
		"kb:t": "dispatchEventNext",
		"kb:shift+t": "dispatchEventPrevious",
		"kb:k": "dispatchEventNext",
		"kb:shift+k": "dispatchEventPrevious",
		"kb:n": "dispatchEventNext",
		"kb:shift+k": "dispatchEventPrevious",
		"kb:f": "dispatchEventNext",
		"kb:shift+f": "dispatchEventPrevious",
		"kb:u": "dispatchEventNext",
		"kb:shift+u": "dispatchEventPrevious",
		"kb:v": "dispatchEventNext",
		"kb:shift+v": "dispatchEventPrevious",
		"kb:e": "dispatchEventNext",
		"kb:shift+e": "dispatchEventPrevious",
		"kb:b": "dispatchEventNext",
		"kb:shift+b": "dispatchEventPrevious",
		"kb:x": "dispatchEventNext",
		"kb:shift+x": "dispatchEventPrevious",
		"kb:c": "dispatchEventNext",
		"kb:shift+c": "dispatchEventPrevious",
		"kb:r": "dispatchEventNext",
		"kb:shift+r": "dispatchEventPrevious",
		"kb:q": "dispatchEventNext",
		"kb:shift+q": "dispatchEventPrevious",
		"kb:s": "dispatchEventNext",
		"kb:shift+s": "dispatchEventPrevious",
		"kb:m": "dispatchEventNext",
		"kb:shift+m": "dispatchEventPrevious",
		"kb:g": "dispatchEventNext",
		"kb:shift+g": "dispatchEventPrevious",
		"kb:d": "dispatchEventNext",
		"kb:shift+d": "dispatchEventPrevious",
		"kb:o": "dispatchEventNext",
		"kb:shift+o": "dispatchEventPrevious",
		"kb:1": "dispatchEventNext",
		"kb:shift+1": "dispatchEventPrevious",
		"kb:2": "dispatchEventNext",
		"kb:shift+2": "dispatchEventPrevious",
		"kb:3": "dispatchEventNext",
		"kb:shift+3": "dispatchEventPrevious",
		"kb:4": "dispatchEventNext",
		"kb:shift+4": "dispatchEventPrevious",
		"kb:5": "dispatchEventNext",
		"kb:shift+5": "dispatchEventPrevious",
		"kb:6": "dispatchEventNext",
		"kb:shift+6": "dispatchEventPrevious"
	}	
