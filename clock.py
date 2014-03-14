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
# 	Snooze button on bottom that does nothing if alarm 
# 		is not going off, else snoozes
#	Set the sound wave for the alarm
#-----------------------------------------------------
from datetime import datetime
import winsound
import time
import wx

class AlarmFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(-1,-1))
		self.CreateStatusBar()
		
		# Setting up the menu.
		filemenu = wx.Menu()
		menuSetAlarm = filemenu.Append(wx.ID_NEW, "Set Alarm", " Set time for alarm")
		menuSetSnooze = filemenu.Append(wx.ID_EDIT, "Set Snooze", " Set length of time for snooze")
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
		menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File")
		self.SetMenuBar(menuBar)
		
		#Events
		self.Bind(wx.EVT_MENU, self.OnAbout, menuSetAlarm)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuSetSnooze)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

		panel = wx.Panel(self)
	
		#Add components to the panel
		self.time = wx.StaticText( panel, label="Time will go here")
		snoozebutton = wx.Button(self, wx.ID_CLEAR, "snooze")
		self.Bind(wx.EVT_BUTTON, self.Snooze, snoozebutton)
		
		self.alarmtoggle = wx.CheckBox(self, label = "alarm ")
		self.Bind( wx.EVT_CHECKBOX, self.ToggleAlarm, self.alarmtoggle)
		
		self.sizerbuttons = wx.BoxSizer(wx.HORIZONTAL)
		self.sizerbuttons.Add(self.alarmtoggle, 0, wx.ALIGN_LEFT)
		self.sizerbuttons.Add(snoozebutton, 1, wx.EXPAND)
		
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.time, 3, wx.ALIGN_CENTER )
		self.sizer.Add(self.sizerbuttons, 1, wx.GROW)
		
		#Layout sizers
		self.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		self.sizer.Fit(self)
		
		self.Show()
		
	def OnAbout(self,e):
		# Create a message dialog box
		dlg = wx.MessageDialog(self, " An Alarm Clock using wxPython", "About Alarm Clock", wx.OK)
		dlg.ShowModal() # Shows it
		dlg.Destroy() # finally destroy it when finished.
 
	def OnExit(self,e):
		self.Close(True)  # Close the frame.

	def Snooze(self,e):
		# Create a message dialog box
		dlg = wx.MessageDialog(self, " Hit Snooze", "Snooze Dialog", wx.OK)
		dlg.ShowModal() # Shows it
		dlg.Destroy() # finally destroy it when finished.

	def ToggleAlarm(self,e):
		# Create a message dialog box
		dlg = wx.MessageDialog(self, " Toggle Alarm", "Alarm Dialog", wx.OK)
		dlg.ShowModal() # Shows it
		dlg.Destroy() # finally destroy it when finished.
	
app = wx.App(False)
frame = AlarmFrame(None, title="Alarm Clock")
app.MainLoop()

#print datetime.now().time()

#winsound.Beep(30000,10000)
#while True:
#	print datetime.now().time()
#	winsound.MessageBeep()
#	time.sleep(10)