#------------------------------------------------------
#
# Alarm clock
#
#	Open a window with the time that changes
#		every second. 
#   Filemenu will open a dialog to set an alarm 
#		and snooze time.
#   The screen shall have a toggle to turn on
#		the alarm and off
# 	A new window should pop-up to allow alarm to
#		be dismissed or snooze button
#	Set the sound wave for the alarm
#-----------------------------------------------------
from datetime import datetime
import winsound
import time
import wx, os

class AlarmFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(-1,-1))
		self.CreateStatusBar()
		
		# Setting up the menu.
		filemenu = wx.Menu()
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
		menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File")
		self.SetMenuBar(menuBar)
		
		#Events
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		
		self.Show()
		
		def OnAbout(self,e):
			# Create a message dialog box
			dlg = wx.MessageDialog(self, " An Alarm Clock using wxPython", "About Alarm Clock", wx.OK)
			dlg.ShowModal() # Shows it
			dlg.Destroy() # finally destroy it when finished.
 
		def OnExit(self,e):
			self.Close(True)  # Close the frame.

class AlarmPanel(wx.Panel):
	
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		self.text_title = wx.StaticText(self, label="Alarm Clock", pos=(20,30))
		
		self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
		
		# Checkbox
		self.alarm = wx.CheckBox( self, label = "Alarm On ", pos=(20, 50))
		self.Bind( wx.EVT_CHECKBOX, self.EvtCheckBox, self.alarm )
		
			
	def EvtCheckBox(self, e):
		self.logger.AppendText('EvtCheckBox: %d\n' %e.Checked())
	
app = wx.App(False)
frame = AlarmFrame(None, title="Alarm Clock")
#panel = AlarmPanel(frame)
frame.Show()
app.MainLoop()

#print datetime.now().time()

#winsound.Beep(30000,10000)
#while True:
#	print datetime.now().time()
#	winsound.MessageBeep()
#	time.sleep(10)