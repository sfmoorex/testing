from tlist import tcommands

def doCommand(cmd):
	App.focus("FieldWorks")
	setAutoWaitTimeout(30)
	print tcommands[cmd]
	for action in tcommands[cmd]:
		#hover(click(wait(action[1])))
		print wait(action[1])
		print Env.getMouseLocation()


for cmd in tcommands:
	print cmd
	doCommand(cmd)


