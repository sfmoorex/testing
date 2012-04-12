App.focus("FieldWorks")
setAutoWaitTimeout(30)
def typeN(num, *args):
	for i in range(num):
		type(*args)


def ProjectLocationsAndSharing():
	type("f", KeyModifier.ALT)
	typeN(3,Key.DOWN)
	type(Key.RIGHT)
	typeN(3,Key.DOWN)
	type(Key.ENTER)
	typeN(2,Key.TAB)
	type(Key.ENTER)

ProjectLocationsAndSharing()

def datas():
	type("v", KeyModifier.ALT); typeN(1,Key.DOWN); type(Key.RIGHT); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(1,Key.DOWN); type(Key.RIGHT); typeN(1,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(1,Key.DOWN); type(Key.RIGHT); typeN(2,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(1,Key.DOWN); type(Key.RIGHT); typeN(3,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(1,Key.DOWN); type(Key.RIGHT); typeN(4,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(1,Key.DOWN); type(Key.RIGHT); typeN(5,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(1,Key.DOWN); type(Key.RIGHT); typeN(6,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(1,Key.DOWN); type(Key.RIGHT); typeN(7,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(2,Key.DOWN); type(Key.RIGHT); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(2,Key.DOWN); type(Key.RIGHT); typeN(1,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(2,Key.DOWN); type(Key.RIGHT); typeN(2,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(2,Key.DOWN); type(Key.RIGHT); typeN(3,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(2,Key.DOWN); type(Key.RIGHT); typeN(4,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(2,Key.DOWN); type(Key.RIGHT); typeN(5,Key.DOWN); type(Key.ENTER);sleep(3)
	type("v", KeyModifier.ALT); typeN(2,Key.DOWN); type(Key.RIGHT); typeN(6,Key.DOWN); type(Key.ENTER);sleep(3)

datas()
