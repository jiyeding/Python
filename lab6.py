''' Jiye Ding'''
'''1.	A function to read from the rawdata_2002.txt file, which is a text version of the population growth page above. 
Each line of the file has 3 fields, separated by colon ( : ).  
Parse each line of data and store the country name as a key and the growth rate as value in a dictionary. 
The ranking field is discarded. The input file should only be accessed by this function.
2.	Since some of the country names may be difficult for the user to remember the exact spelling (Herzegovina? Vanuatu?), 
whenever the user enters a single letter at the search prompt, 
print all the country names that have the same starting letter. 
Write a function that creates a dictionary with keys that are first letters of the countries, 
and the value of each key is a set of country names with the same starting letter. 
For example, the key 'Z' has a value which is the set (Zambia, Zimbabwe).
3.	A function that loops to let the user enters in a full country name or a letter. 
If the user enters a name, print the corresponding growth rate. 
If the user enters a letter, print the set of country names that have a matching starting letter. 
If the name or the letter doesn't exist, print an error message.'''

def main():       ####### country() is the main function, do not need this one !!!!!!
    country()
    ### it should be:
    #dic = countryRate()
    #let = firstLetter()
    #country = (dic,let)
        
'''main function to call below three function'''
    
def countryRate():
    try :
        with open("lab6Input.txt") as infile:
            countryrate = {}
            line = infile.readline()
            for line in infile:       
                words = line.rstrip().split(":")
                countryrate[words[1].upper()] = words[2]   
        return countryrate
    except IOError:
        print("Error opening" + DEFAULT_FILE)      # DEFAULT_FILE = "    .txt"
        raise SystemExit        # considered better practixe than : exit()       quit()
                                 #can also use: sys.exit()     if you import sys at the top

'''A function to read from the rawdata_2002.txt file, which is a text version of the population growth page above. 
Each line of the file has 3 fields, separated by colon ( : ).  
Parse each line of data and store the country name as a key and the growth rate as value in a dictionary. 
The ranking field is discarded. The input file should only be accessed by this function.'''

def firstLetter():
    # Pythonic way
    ##letters = {}
    ##for country in growthRate :
        ##try :
            ##letters[country[0]].add(country)          209 times
        ##except KeyError :
            ##letters[country[0]]] = set([country])    26 exceptions
    
    firstletter = {}
    for key in countryRate() :
        if key[0] in firstletter :                                  
            firstletter[key[0].upper()].add(key.upper())
        else :
            firstletter[key[0].upper()] = set()
            firstletter[key[0].upper()].add(key.upper()) 
    ''' below is the way access the file'''
    #with open("lab6Input.txt") as infile:
        #firstletter = {}
        #line = infile.readline()
        #for line in infile:       
            #words = line.rstrip().split(":")
            ##firstletter[words[1][0]] = set(words[1])       
            #if words[1][0] in firstletter:
                #firstletter[words[1][0]].add(words[1]) 
            #else:    
                #firstletter[words[1][0]] = set()
                #firstletter[words[1][0]].add(words[1])
    return firstletter

'''Since some of the country names may be difficult for the user to remember the exact spelling (Herzegovina? Vanuatu?), 
whenever the user enters a single letter at the search prompt, 
print all the country names that have the same starting letter. 
Write a function that creates a dictionary with keys that are first letters of the countries, 
and the value of each key is a set of country names with the same starting letter. 
For example, the key 'Z' has a value which is the set (Zambia, Zimbabwe).'''

def country():
    country = False
    while not country :
        country = input("Enter a country name (or type quit to quit): ")         ## country = input().upper
        if not country.isupper() :
            country = country.upper()
        if country in countryRate() :                   
            print("The growth rate is " + str(countryRate()[country]))
            country = False
        elif country in firstLetter() :
            for country in sorted(firstLetter()[country]):             
                print(country)
            country = False
        elif country == "QUIT" :
            country = True
        else :
            print("No such country name.")
            country = False
            
        # if len(country) == 1 and country in.....
        ## use len to check 1 dictionary, no need to check both dictionary!!!
        
        ## Pythonic way
        ##if len(country) == 1:
            ##try :
                ##print("\n".join(sorted(letters[country])))      # print a list in a line
            ##except KeyError :
                ##print("No Countryies start with that letter")
        ##else :
            
    
    
'''A function that loops to let the user enters in a full country name or a letter. 
If the user enters a name, print the corresponding growth rate. 
If the user enters a letter, print the set of country names that have a matching starting letter. 
If the name or the letter doesn't exist, print an error message.'''

main()