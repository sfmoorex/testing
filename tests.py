from tlists import tcommands
anywhere = Region(0,24,1680, 1050)
cmdregion = Region(0,24,950,300)
foundregion = cmdregion

def changed(event):
	global foundregion
	foundregion = event.changes[0]
	print
	for e in event.changes:
		print "found", e
	anywhere.stopObserver()
	

def doCommand(cmd):
	App.focus("FieldWorks")
	setAutoWaitTimeout(30)
	print cmd
	cmdregion = (0,24,950,300)
	for action in cmd[1]:
		click(foundregion.find(action[1]))
		anywhere.observe(5)

		#hover(click(wait(action[1])))
		#print wait(action[1])
		#print Env.getMouseLocation()


for cmd in tcommands:
	global anywhere
	global cmdregion
	global foundregion 
	foundregion = cmdregion
	anywhere.onChange(5000,changed)
	anywhere.observe(background = True)
	print cmd
	doCommand(cmd)
	print "foundregion is", foundregion
	res = foundregion.exists("cancel.png",20)
	if res:
		click(res)
	#cmdregion.stopObserver()


