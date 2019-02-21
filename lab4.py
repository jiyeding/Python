'''Jiye Ding'''

'''1.	main:  loop to let the user keep entering zip codes and seeing the barcodes, until the user chooses 0. The 0 is a sentinel, when the user enters 0, the loop stops and the program ends.
2.	getZipCode: prompt the user for a 5-digit zip code. Check that the user input is a 5 digit number or a 0, otherwise keep prompting until you get a valid input..
3.	printDigit: accept 1 digit as input argument and print the equivalent barcode.
4.	printBarCode: print the starting and ending full bars, and call the printDigit function to print each of the 6 digits in between.
'''


def main():
    ZipCode = input("Enter 5-digit zip code or 0 to end: ")
    while ZipCode != "0":
        if getZipCode(ZipCode) == True:
            print(printBarCode(ZipCode))
        ZipCode = input("Enter 5-digit zip code or 0 to end: ")

''' loop to let the user keep entering zip codes and seeing the barcodes, until the user chooses 0. 
The 0 is a sentinel, when the user enters 0, the loop stops and the program ends. '''  



def getZipCode(ZipCode):
    if ZipCode.isdigit() and len(ZipCode) == 5:        ### while not zipcode.isdigit() or len    !5 or       !=0 :
        return True
    else:
        print("Zip code must be a 5-digit number")
        return False

'''prompt the user for a 5-digit zip code. Check that the user input is a 5 digit number or a 0, 
otherwise keep prompting until you get a valid input..'''

        
def printDigit(i):
    if i == "0":
        return "||:::"
    elif i == "1":
        return ":::||"
    elif i == "2":
        return "::|:|"
    elif i == "3":
        return "::||:"
    elif i == "4":
        return ":|::|"
    elif i == "5":
        return ":|:|:"
    elif i == "6":
        return ":||::"
    elif i == "7":
        return "|:::|"
    elif i == "8":
        return "|::|:"
    elif i == "9":
        return "|:|::"

'''  accept 1 digit as input argument and print the equivalent barcode.'''


#barcodes = ["|:|::", "", "",...]
#print(barcode[digit])

        
def printBarCode(ZipCode):
    sum = 0
    ZipCode = str(ZipCode)
    for n in range(0,5):    ### use len(ZipCode instead of 5)
        sum += int(ZipCode[n])       
    if sum%10 == 0:
        sixth = "0"
    else:
        sixth = str(10 - sum%10)        # six is the 6th digit
    ZipCode = ZipCode + sixth         # total 6 digits zipcode
    printBarCode = "|"
    for i in range(0,6):
        printBarCode += printDigit(ZipCode[i])
    printBarCode = printBarCode + "|"
    return printBarCode
 
''' print the starting and ending full bars, and call the printDigit function to print each of the 6 digits in between.'''       



main()
