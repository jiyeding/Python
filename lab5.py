''' Jiye Ding '''

'''The program has a main function that calls 3 other functions (there are 5 functions total): 
1.	Call readChart() to:
•	Read in the data from the input file and stores it in a seating chart, which is a list of lists, where each inner 
list is a row of data of the input file. The input file can be a filename that the user enters or the default lab5input.txt 
if the user hits Enter. 
•	call printChart() to print the seating chart. See the sample output for printing format.
2.	Call buySeat() to:
•	Ask the user for the number of seats that he/she wants to buy. 
•	For each seat that the user buys, ask for the (row,col) location and check that the seat is still available. 
If it's available:
o	add up the price of the seat
o	mark the seat with an 'X' to show that it's taken
o	save the seat (row, col) location as a tuple in a list of tuples
If it's not available, keep asking for a new (row,col) location
•	When all seats are chosen, print out the total price for all the seats, all the seat locations as (row,col) tuples, 
and call printChart() to print the updated seating chart. See sample output.
3.	Call saveChart() to:
•	Save the seating chart to an output file or back to the default lab5input.txt file. Choose the default
file if the user hits Enter instead of typing in a filename. 
•	When saving the seating chart, the 'X' is saved as '-' (a dash)
'''


def main() :
    chart = []         ### dont need to create empty chart, create in readChart()
    while chart == [] :
        chart = readChart(chart)
    print("Available seats are shown with price")
    chart = buySeat(chart)
    saveChart(chart)
    
         
def readChart(chart) :    ### use a loop to instead a recursive call!!!
    try :     
        filename = input("Enter file name or hit Enter for default lab5input.txt: ")
        if filename == "":
            filename = "lab5input.txt"
            #filename = "lab5output.txt"             
        with open(filename) as infile :
            #row = []
            #row = infile.readline().rstrip().split() 
            aline = infile.readline()
            try :      
                if aline == "" :
                    raise ValueError("file empty")        # file empty error 
                n = 0
                while aline != "" :
                    aline = aline.rstrip()
                    alinelist = aline.split()       
                    m = len(alinelist)      # number of col will be used in printChart()
                    n += 1                  # number of row will be used in printChart() 
                    chart.append(alinelist)
                    aline = infile.readline()                          
                printChart(m,n,chart)   
            except ValueError :              
                print("file empty")
                #readChart(chart)                
    except IOError :
        print("file not found")             # file not found error
        #readChart(chart)
    return chart
'''•	Read in the data from the input file and stores it in a seating chart, which is a list of lists, where each inner 
list is a row of data of the input file. The input file can be a filename that the user enters or the default lab5input.txt 
if the user hits Enter. 
•	call printChart() to print the seating chart. See the sample output for printing format.'''
    
             
def printChart(m,n,chart): 
    print()
    print("Price chart".center(59))
    print("Column".center(57))
    print(" "*7, end = "")
    chart2 = []
    chart2 = [list(chart[row]) for row in range(n)] 
    for col in range(m-2):
        print(str(col+1) + " "*4, end = "")
    print(str(m-1) + " "*3 + str(m))
    print("Row  " + "="*50)
    for row in range(n):
        for col in range(m):
            if str(chart2[row][col]).isdigit():
                chart2[row][col] = "$"+str(chart2[row][col])           # add $ for every emelent in the chart2    
            else:
                chart2[row][col] = "  "+str(chart2[row][col])            # add "   " for "-" and "X"in the chart2
    for row in range(n):
        print (" " + str(row+1) + " |  "+ '  '.join(chart2[row]))  
    


      
    

def buySeat(chart) :
    try :
        numseat = input("Number of seats: ")
        m = len(chart[1])      # number of col will be used in printChart()
        n = len(chart)                  # number of row will be used in printChart()         
        seatBought = 0
        x = 0
        y = 0        
        for x in range(n):
            for y in range(m):
                if str(chart[x][y]).isdigit() != True:
                    seatBought += 1  
        if int(numseat) < int(0) or int(numseat) > int((90-seatBought)):  
            raise ValueError("wrong seat number")
        price = 0
        list = []
        i = 1
        while i >=1 and i <= int(numseat) :
            j = str(i)
            try : 
                position = input("Enter row,col for seat "+ j + ": ")
                a = position.index(",")     #location of ","
                row = ""
                col = ""
                for j in range(a) :
                    row += position[j]
                for j in range(a+1, len(position)) :
                    col += position[j]
                row = int(row)
                col = int(col)
                if row > 9 or col > 10 or row < 1 or col < 1 :                 ## invalid row or col error
                    ### use size of the chart!!!
                    print("Invalid row or column")
                    i = i            
                elif chart[row-1][col-1] != "-" and chart[row-1][col-1] != "X":
                    price += int(chart[row-1][col-1])    # add up the price
                    chart[row-1][col-1] = "X"        # mark "X"
                    list.append((row,col))          # save to list of tuples
                    i += 1   
                else :
                    print("Sorry, that seat is not available.")
                    i = i
            except ValueError :
                print("Rows and columns must be numbers")
                i = i
        price = "$"+str(price)
        print("Your total: " + price)
        numseat = str(numseat)
        print("Your " + numseat + " seat(s) are at ", end = "")
        print(*list, end = "")     # pring a list without [ ]
        print(" are marked with 'X'")
        printChart(m,n,chart)  
    except ValueError as numseat:
        print("The number of seat must be an integer between 1 and", 90-seatBought)    ## size of the chart , not 90!!
        buySeat(chart)
    return chart

'''•	Ask the user for the number of seats that he/she wants to buy. 
•	For each seat that the user buys, ask for the (row,col) location and check that the seat is still available. 
If it's available:
o	add up the price of the seat
o	mark the seat with an 'X' to show that it's taken
o	save the seat (row, col) location as a tuple in a list of tuples
If it's not available, keep asking for a new (row,col) location
•	When all seats are chosen, print out the total price for all the seats, all the seat locations as (row,col) tuples, 
and call printChart() to print the updated seating chart. See sample output.'''

  
def saveChart(chart) :
    filename = input("Enter file name or hit Enter for default lab5input.txt: ")
    if filename == "":
        filename = "lab5input.txt"
        #filename = "lab5output.txt"
        print("lab5input.txt updated")   
    with open(filename, "w") as outfile :
        lines = ""
        for j in range(len(chart)) :         # row 
            for i in range(len(chart[j])) :     # col 
                if chart[j][i] == "X" :
                    chart[j][i] = "-"          # change "X" to "-"
                lines += chart[j][i] + " "
            lines = lines + "\n"        # transfer a table(list) to a string because .write(string) 
        outfile.write(lines)

'''•	Save the seating chart to an output file or back to the default lab5input.txt file. Choose the default
file if the user hits Enter instead of typing in a filename. 
•	When saving the seating chart, the 'X' is saved as '-' (a dash)'''

main()