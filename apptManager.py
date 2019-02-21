''' Jiye Ding'''

'''Create a file called apptManager.py, which contains an ApptManager class. This class has the following methods:
•	A public processChoice method that will:
o	 print a menu to add, list, or quit
o	read in the user choice
o	process the user's menu choice
Keep looping to ask for a choice if the choice is not valid (see sample output).
•	A private getDate method that asks for a month and day. 
Keep looping to ask for input until there is a valid month and day (see sample output).
•	A private addAppointment method that will:
o	call the getDate method to get the appointment date
o	ask for the event name and the type of event (one-time, daily, monthly). 
Keep looping if the user doesn't enter the correct type (see sample output).
o	create the correct type of appointment object and store it
•	A private listAppointment method that:
o	prints a "no appointment" if there nothing has been scheduled
o	call getDate to get a month / day
o	print all appointments that will occur on that month / day
'''


## private function should have "_" and cannot be called outseide the class !!!

from appointment import Appointment, Onetime, Daily, Monthly

class ApptManager :
    def processChoice(self, appointment = []) :
        self._choice = ""
        self._appointment = appointment
        while self._choice != "q" :
            self._choice = str(input("a. add, l. list, q. quit.\nYour choice? "))
            while self._choice != "a" and self._choice != "l" and self._choice != "q":
                print("choice a, l, q only")
                print()
                self._choice = str(input("a. add, l. list, q. quit.\nYour choice? "))
            if self._choice == "a" :
                print("New appointment")
                self._appointment.append(ApptManager()._addAppointment())
                print()
            if self._choice == "l" :
                ApptManager()._listAppointment(self._appointment) 
                print()
                
            '''•	A public processChoice method that will:
                o	 print a menu to add, list, or quit
                o	read in the user choice
                o	process the user's menu choice
                Keep looping to ask for a choice if the choice is not valid (see sample output).'''


    def _getDate(self) :
        self._month = ""
        self._day = ""
        while self._month == "" or self._day == "" :
            try :
                self._month = int(input("month: "))
                if self._month < 1 or self._month >12 :
                    raise ValueError
                self._day = int(input("day: "))
                if self._month in [1,3,5,7,8,10,12] and self._day < 1 or self._day > 31:
                    self._day = ""
                    raise ValueError
                if self._month in [4,6,9,11] and self._day < 1 or self._day > 30 :
                    self._day = ""
                    raise ValueError
                if self._month == 2 and self._day < 1 or self._day >28 :
                    self._day = ""
                    raise ValueError
            except ValueError :
                print("day and month must be valid integers")
        return (self._month, self._day)
    
    '''•	A private getDate method that asks for a month and day. 
Keep looping to ask for input until there is a valid month and day (see sample output).
    '''
        
    def _addAppointment(self) :
        self._date = ApptManager()._getDate()
        self._eventname = input("Name: ")       
        self._type_event = str(input("o. onetime, d. daily, or m. monthly? "))
        while self._type_event != "o" and self._type_event != "d" and self._type_event != "m" :
            self._type_event = input("o. onetime, d. daily, or m. monthly? ")  
        return (self._date[0], self._date[1], self._eventname, self._type_event)
                       
    '''•	A private addAppointment method that will:
o	call the getDate method to get the appointment date
o	ask for the event name and the type of event (one-time, daily, monthly). 
Keep looping if the uAser doesn't enter the correct type (see sample output).
o	create the correct type of appointment object and store it'''
        
    def _listAppointment(self, appointment) :
        if appointment == [] :
            print("There is no appointment scheduled") 
        else :
            print("List appointment(s) for")
            self._date = ApptManager()._getDate()
            # count = 0
            for i in range(len(appointment)) :
                if appointment[i][3] == "o" :
                    object = Onetime(month = appointment[i][0], day = appointment[i][1], eventname = appointment[i][2])
                    if object.occursOn(self._date) == True:
                        print(object)        
                elif appointment[i][3] == "d" :
                    object = Daily(month = appointment[i][0], day = appointment[i][1], eventname = appointment[i][2])
                    if object.occursOn(self._date) == True:
                        print(object)                        
                elif appointment[i][3] == "m" :
                    object = Monthly(month = appointment[i][0], day = appointment[i][1], eventname = appointment[i][2])
                    if object.occursOn(self._date) == True:
                        print(object)   
                        
                        
            ### if count ==o : print : no appointment on that day
        
        '''• A private listAppointment method that:
    o	prints a "no appointment" if there nothing has been scheduled
    o	call getDate to get a month / day
    o	print all appointments that will occur on that month / day'''
                
