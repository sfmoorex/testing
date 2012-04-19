from sikuli import *
import os



def ctrl(key):
	type(key,KeyModifier.CTRL)
def alt(key):
	type(key,KeyModifier.ALT)
def ek():
	type(Key.ENTER)

def rk():
	type(Key.RIGHT)
def lk():
	type(Key.LEFT)
def uk():
	type(Key.UP)
def dk(n):
	for i in range(n): 
		type(Key.DOWN)

def findPattern(filename,doClick=False):
	newfilename =  "imageFiles/" + filename + ".png"
	print "finding:", newfilename
	if os.access(newfilename ,os.R_OK) == False:
		sleep(5) # give things time to settle down
		print "Capture pattern for " + filename
		f = capture("Please outline the pattern for " + filename)
		os.rename(f,newfilename )
		#App.focus("FieldWorks")
	m = exists(newfilename)
	if doClick:
		return click(m)
	else:
		return m

def getReady():
	App.focus("FieldWorks")
	setAutoWaitTimeout(60)
	findPattern("FieldWorksReady")
	setAutoWaitTimeout(10)

#used for bringing up all of the View menu areas except Lists
def switchView(menuKey,menuCategory,menuItem,stepsDown):
	getReady()
	alt("v")
	findPattern("viewmenus")
	type(menuKey)
	findPattern(menuCategory + "Menu")
	dk(stepsDown)
	ek()
	findPattern(menuCategory + menuItem + "Ready")
	print "Done:" + menuItem



#lists don't work so well different, no telling why
def listsSwitchView(menuKey,menuCategory,menuItem,stepsDown):
	findPattern("ListButton",True)
	findPattern("ListMenuReady")
	findPattern("Lists" + menuItem + "ClickOn",True)
	findPattern(menuCategory + menuItem + "Ready")
	print "Done:" + menuItem



def showListsViews():
	listsSwitchView("s","Lists", "AcademicDomains", 0 )
	listsSwitchView("s","Lists", "AnthropologyCategories", 1 )
	listsSwitchView("s","Lists", "ComplexFormTypes", 2 )
	listsSwitchView("s","Lists", "ConfidenceLevels", 3 )
	listsSwitchView("s","Lists", "EducationLevels", 4 )
	listsSwitchView("s","Lists", "FeatureTypes", 5 )
	listsSwitchView("s","Lists", "Genres", 6 )
	listsSwitchView("s","Lists", "LexicalRelations", 7 )
	listsSwitchView("s","Lists", "Locations", 8 )
	listsSwitchView("s","Lists", "MorphemeTypes", 9 )
	listsSwitchView("s","Lists", "NotebookRecordTypes", 10 )
	listsSwitchView("s","Lists", "People", 11 )
	listsSwitchView("s","Lists", "Positions", 12 )
	listsSwitchView("s","Lists", "Publications", 13 )
	listsSwitchView("s","Lists", "Restrictions", 14 )
	listsSwitchView("s","Lists", "ReversalIndexCategories", 15 )
	listsSwitchView("s","Lists", "Roles", 16 )
	listsSwitchView("s","Lists", "SemanticDomains", 17 )
	listsSwitchView("s","Lists", "SenseTypes", 18 )
	listsSwitchView("s","Lists", "Status", 19 )
	listsSwitchView("s","Lists", "TextChartMarkers", 20 )
	listsSwitchView("s","Lists", "TextConstituentChartTemplates", 21 )
	listsSwitchView("s","Lists", "TextMarkupTags", 22 )
	listsSwitchView("s","Lists", "TimeOfDay", 23 )
	listsSwitchView("s","Lists", "TranslationTypes", 24 )
	listsSwitchView("s","Lists", "Usages", 25 )
	listsSwitchView("s","Lists", "VariantTypes", 26 )

def showNotebookViews():
	switchView("n","Notebook","RecordEdit",0)
	switchView("n","Notebook","Browse",1)
	switchView("n","Notebook","Document",2)

def showTextViews():
	switchView("t","Texts","Interlinear",0)
	switchView("t","Texts","Concordance",1)
	switchView("t","Texts","WordListConcordance",2)
	switchView("t","Texts","WordAnalyses",3)
	switchView("tC:\Users\lsdeveloper\testing\mm.sikuli\imageFiles\OK.png","Texts","BulkEditWordForms",4)
	switchView("t","Texts","Statistics",5)

def showLexiconViews():
	switchView("l","Lexicon","Edit",0)
	switchView("l","Lexicon","Browse",1)
	switchView("l","Lexicon","Dictionary",2)
	switchView("l","Lexicon","Categorized",3)
	switchView("l","Lexicon","Classified",4)
	switchView("l","Lexicon","BulkEdit",5)
	switchView("l","Lexicon","Reversal",6)
	switchView("l","Lexicon","BulkEditReversal",7)

def showGrammarViews():
	switchView("g","Grammar","GrammarSketch",11)
	switchView("g","Grammar","Problems",12)
	switchView("g","Grammar","CategoryEdit",0)
	switchView("g","Grammar","CategoryBrowse",1)
	switchView("g","Grammar","CompoundRules",2)
	switchView("g","Grammar","Phonemes",3)
	switchView("g","Grammar","PhonologicalFeatures",4)
	switchView("g","Grammar","NaturalClasses",5)
	switchView("g","Grammar","Environments",6)
	switchView("g","Grammar","PhonologicalRules",7)
	switchView("g","Grammar","AdHocRules",8)
	switchView("g","Grammar","InflectionFeatures",9)
	switchView("g","Grammar","ExceptionFeatures",10)


def menuReady(altKey,readyPattern):
	getReady()
	alt(altKey)
	findPattern(readyPattern)


def newProject():
	menuReady("f","FileMenu")
	type("n")
	findPattern("NewProjectDialog")
	findPattern("Cancel",True)
	print "Done:" + "NewProjectDialog"

	
def openProject():
	menuReady("f","FileMenu")
	ctrl("o")
	findPattern("OpenFileDialog")
	findPattern("OpenCancel",True)
	print "Done:" + "OpenProjectDialog"

def projectProperties():
	menuReady("f","FileMenu")
	type("m")
	findPattern("propertiesMenu")
	type("w")
	findPattern("propertiesDialog")
	findPattern("propertiesCancel",True)
	print "Done:" + "ProjectProperties"

def InsertLexiconGoSimilar():
	menuReady("i","InsertMenu")
	ctrl("e")
	findPattern("LexiconInsertDialog")
	findPattern("LexemeFormEntry",True)
	type("cadu")
	findPattern("caduInList",True)
	findPattern("SimilarEntries",True)

def ConfigureDictionary():
	switchView("l","Lexicon","Edit",0)
	menuReady("t", "Tools")
	type("c")
	type("d")
	findPattern("DictConfigDialog")
	findPattern("HomoGraphCheck",True)
	findPattern("HomographConfig")
	findPattern("DisplayHomograph",True)
	findPattern("CharacterStyle",True)
	findPattern("CharacterStylesList")
	findPattern("EmphasizedText",True)
	findPattern("DictConfigCancel",True)

def FindWordFormConcordance():
	switchView("t","Texts","WordListConcordance",2)
	ctrl("f")
	findPattern("FindWordForm")
	findPattern("WordFindBox",True)
	type("munalongera")
	findPattern("GoTo",True)
	ctrl("f")
	findPattern("FindWordForm")
	findPattern("WordFindBox",True)
	type("tiri")
	findPattern("GoTo",True)
	findPattern("SVOWarning")
	findPattern("OK", True)
	ctrl("f")
	findPattern("FindWordForm")
	findPattern("WordFindBox",True)
	type("ukakwate")
	findPattern("GoTo",True)






	
FindWordFormConcordance()
showLexiconViews()
ConfigureDictionary()
InsertLexiconGoSimilar()
newProject()
openProject()
projectProperties()
#showListsViews()
#showNotebookViews()
#showTextViews()
#showGrammarViews()
