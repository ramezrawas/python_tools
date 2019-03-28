import os
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
import json
##############################################################
# open the XML file, convert to json and dump into a new file#
##############################################################
def xml_to_json(input, output):
    
    i = 0
    template_output = output
    
    #################################################################
    #BadgerFish(bf): Use "$" for text content, @ to prefix attributes
    #fromstring: barses an XML section from a string constant
    #################################################################
    with open(input+ ".xml", "r") as input:
        jsonOut = bf.data(fromstring(input.read()))
        
        #############################################################################################
        #Check if the name of the output file is already exists.
        #If it exits, it will add incrementing suffix depending on how many copies are already there.
        #############################################################################################
        while(os.path.isfile(output+'.json')==True):
            print("lastoutput"+output[-1])
            print("i "+str(i))
            if(output == template_output):
                output+=str(i)
            else:
                output = template_output
                output+=str(i)
            i+=1

    with open(output+ ".json","w+") as newFile:
            json.dump(jsonOut, newFile, ensure_ascii=False)
        
#Implementation...
xml_to_json(input('The .xml file: '), input('The .json file: '))
