from sikuli import *
from tlists import tcommands
anywhere = Region(0,24,1680, 1050)
cmdregion = Region(0,24,950,300)
foundregion = cmdregion
watchfor = "impossible string"

def changed(event):
	print "entering chnaged"
	global foundregion
	global watchfor
	print foundregion
	for e in event.changes:
		foundregion = e
		found = e.exists(watchfor)
		if found:
			print "found a match", found
			watchfor = "continue on"
	

def doCommand(cmd):
	global anywhere
	print "the command is:", cmd[1][1:]
	print "the whole command is", cmd
	global watchfor
	App.focus("FieldWorks")
	setAutoWaitTimeout(30)
	click(cmdregion.exists(cmd[1][0][1]))
	for action in cmd[1][1:]:
		watchfor = action[1]
		click(exists(action[1]))
	print "watchfor=",watchfor
	#anywhere.stopObserver()

		#hover(click(wait(action[1])))
		#print wait(action[1])
		#print Env.getMouseLocation()


anywhere.onChange(5000,changed)
anywhere.observe(background = True)

for cmd in tcommands:
	global anywhere
	global cmdregion
	global foundregion 
	global watchfor
	watchfor = "impossible string"
	foundregion = cmdregion
	doCommand(cmd)
	#print "foundregion is", foundregion
	#res = foundregion.exists("cancel.png",20)
	#if res:
	#	click(res)


