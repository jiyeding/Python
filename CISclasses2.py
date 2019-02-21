'''Jiye Ding'''


import re

class CISclasses:
    
    def __init__(self, classes = {},quarters = {}) :         
        self._classes()
        self._quarters()    
    ''' two dictionary: 1. classes: classes as key      2. quarters: quarters as key'''   
    
    def _classes(self) :
        with open("cis_classes.txt") as infile:       
            self._classes = {}
            aline = infile.readline()
            n = 0
            for aline in infile:
                aline = aline.rstrip()
                classname1 = re.search('Num=[CIS|ACCT][\w\d\-_]*">([\w\s\.\+-/#:]+)&?n?b?s?p?;?<?',aline)
                                                            #######[^<]              (&nbsp;)?
                                                            ### use " ( | )" add  the other pattern
                                                            ### then use m.group(2)
                                                            ### can use (sdfsf){1,2}
                classname2 = re.search('catalogID=\d*">([\w\s\.\+-/#:]+)&?n?b?s?p?;?<', aline)
                classname3 = re.search('target="_blank">([\w\s\.\+-/#:]+)&?n?b?s?p?;?<',aline)
                classname4 = re.search('<td>([A-Za-z\s]*)<br',aline)
                classnames = [classname1, classname2, classname3, classname4]
                quarter = ['fall','winter','spring','summer']
                for j in classnames :
                    if j :
                        classname = j.group(1)
                        self._classes[classname] = set()
                        for i in quarter:
                            aline = infile.readline()
                            x = re.search('x', aline)
                            if x:
                                self._classes[classname].add(i) 
        return self._classes
    ''' the first dictionary---classes, read from the cis_classes.txt, key is the classnames, value is set of quarters'''
                
    def _quarters(self) :    #### simpler to have 4 dictionaries, rather than 1 dictionary with 4 sets!!!
        self._quarters = {}
        self._quarters['spring'] = set()
        self._quarters['summer'] = set()
        self._quarters['fall'] = set()
        self._quarters['winter'] = set()
        for key in self._classes:
            for i in self._classes[key] :
                self._quarters[i].add(key)
        return self._quarters         
    ''' the second dictionary---quarters, read from the first dictionary--classes, 
    only four keys in this dictionary, they are four quarters, value is a set of classes in each quarter.'''      
    
    def getCount(self) :
        return len(self._classes)
    ''' count the length of the dictionary classes '''
    
    def getQuarters(self,name) :      
        list = []
        n = 0
        for key in self._classes :
            if name in key :
                list.append(key)
                n += 1
        if n == 0:
            print("0 classes matching " + name)
        else :
            print(str(n) + " classes matching " + name)
            for i in list:
                print(i)
            classname = input("Enter a class name: ")
            while classname not in list:
                print("No class by the name Adv " + classname)
                classname = input("Enter a class name: ")
            if self._classes[classname] == set():
                print(classname + " is not currently offered")
            else :
                print(classname + " will be offered in:",end = "")
                for i in self._classes[classname]:
                    print(" " + i, end = "")
        print()
        ''' print the list of classes searching from the key words,
        print the class searching from the full class name. '''
        
        
    def getClasses(self, quarter) :
        self._quarter = quarter
        if self._quarter != "spring" and self._quarter != "fall" and self._quarter != "winter" and self._quarter != "summer" :
            print("Enter fall, winter, spring, or summer only")
        else :
            print("class in " + self._quarter)
            for i in self._quarters[self._quarter]:
                print(i)
    ''' print the value of the key of the dictionary-quarters, print the set of classes in each quarter'''
        