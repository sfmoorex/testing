require 'nokogiri'
include Nokogiri
require 'pp'
Fwconfigdir  = "C:\\fw\\Language Explorer\\Configuration"

def deriveContext(fn)
	case fn
	when /Grammar/,/Lexicon/,/Lists/,/Notebook/,/Texts/,/Words/
		return Regexp.last_match(0)
	end
	return nil
end
		
def processFile(filename)
  node = XML.parse(File.open(filename)).root
  asDict(node,nil)
end
def asSingleNode(node)
   	out = {"name" => node.name}
	node.attribute_nodes.each { |i| out[i.name] = i.value}
	out
end

def asDict(node,ctxt)
   	out = {"name" => node.name}
   	case node.name
   	when "text", "#comment", "comment"
		return nil
   	when "include"
	   	out = {
		   	"name" => node.name,
		   	"sourceDir" => Dir.pwd,
		   	"path" => node["path"],
		   	"query" => node["query"],
			"absolutePath" => File.dirname(File.absolute_path(node["path"])),
		   	"children" => []
	   	}
	   	pathparts = node["path"].split("/")
	   	if not (pathparts[0] == "Extensions" or pathparts[0] == "$this")
		   	newnode = XML.parse(File.open(node["path"]))
		   	pieces = newnode.xpath(node["query"])
		   	pieces.each { |i|
				returnDir = Dir.pwd
				fileap = File.absolute_path(node["path"])
				Dir.chdir(File.dirname(fileap))
				candidate = asDict(i,deriveContext(fileap))
				if candidate
					out["children"] << candidate
				end
				Dir.chdir(returnDir)
		   	}
	   	end
   	else
	   	out = {
		   	"name" => node.name, 
			"children" => []
	   	}
		if node.name == "command"
			if ctxt == nil
				out["ctxt"] = "General"
			else
				out["ctxt"] = ctxt
			end
		end

	   	node.attribute_nodes.each { |i| out[i.name] = i.value}
	   	if node.children.count > 0 
			m = out["children"]
		   	node.children.each do |child|
			   	candidate = asDict(child,ctxt)
			   	if candidate
				   	m << candidate
			   	end
		   	end
	   	end
   	end
	out
end


def resolveInclude(node)
	ret = node["children"].collect { |i|
		resolveNode(i)
	}
	return ret
end

def resolveNode(node)
	updated = []
	node["children"].each { |i|
		if i["name"] == "include"
			updated = updated +  resolveInclude(i)
		else
			updated = updated + [resolveNode(i)]
		end
	}
	node["children"] = updated
	return node
end



saveDir = Dir.pwd
Dir.chdir(Fwconfigdir)
m = processFile("Main.xml")
Dir.chdir(saveDir)


mfinal = resolveNode(m)

#of1 = File.open("output1.txt", "w+")
#of2 = File.open("output2.txt", "w+")
#of1.write(m.pretty_inspect)
#pp m.class
#of2.write(mfinal.pretty_inspect)
#pp "DONE"

outm = XML::Document.new()

def nativeToXml(x,doc)
	nde = XML::Node.new(x["name"],doc)
	x.each { |k, v|
		case k
		when "name"
			# already taken care of
		when "children"
			v.each { |item|
				nde << nativeToXml(item,doc)
			}
		else
			nde[k] = v
		end
	}
	return nde
end
outm.root =  nativeToXml(mfinal,outm)
outm.write_xml_to File.open("fxml.xml","w+")

def doMenu(cmd,label)
	pp ['menu', cmd, label]
end

def clickMenuItem(cmd,label)
	pp ['item',cmd, label]
end



def genPlan(itm,cmd)
	seq = []
	while itm.class != XML::Document
		seq << asSingleNode(itm)
		itm = itm.parent
	end
	return [asSingleNode(cmd),seq.reverse]
end

def allCommands(outm)
	cmds = []
	outm.xpath("//command").each { |cmd|
		sstr = "//item[@command=\"" + cmd["id"] + "\"]"
		outm.xpath(sstr).each  { |itm|
			cmds << genPlan(itm,cmd)
		}
	}
	cmds
end

def hasItemType(itemtype,dictlist)
	dictlist.each {|i|
		if i["name"] == itemtype
			return true
		end
	}
	return false
end

allcmds = allCommands(outm)

dothese = allcmds.select { |i| 
	i[1].detect { |j| 
		j["name"] == "menubar" 
	}
}.select { |k|
	k[0]["ctxt"] == "General"
}


def analyzeShortcut(str)
	return str + "TODO"
end

def genCode(c)
	cmd = c[0]
	printf("[\"%s\",[" % c[0]["id"])
	path = c[1]
	if cmd["shortcut"] 
		#pp ["shortcut", analyzeShortcut(cmd["shortcut"])]
	elsif cmd["label"] 
		m =  /_(.)/.match(cmd["label"])
		if m
			#pp ["shortcut",analyzeShortcut(m[1])]
	   	else 
			#pp ["shortcut:", cmd["label"]]
		end
	end

	#pp ["#begin exec"]
	path.each { |i|
		#pp ["this is a ",i]
		case i["name"]
		when "menu"
			printf("[\"menu\",\"%s\"]," % i["label"].sub("_",""))
		when "item"
			printf("[\"item\",\"%s\"]," % cmd["label"].sub("_",""))
		end
	}
	printf("]],\n")
	#pp ["#end exec"]
end

printf "tcommands = [\n"
dothese.each { |i| genCode(i) }
printf "]\n"
