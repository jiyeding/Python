''' Jiye Ding'''

'''Create a file called appointment.py, which contains an abstract superclass named Appointment and 3 subclasses named: 
Onetime, Daily, Monthly.
•	The abstract Appointment class constructor requires a month, day, and event argument. 
This superclass requires all subclasses to have an occursOn method.
•	The 3 subclasses all have a __repr__ method to print the object's type of appointment, the date and event (see sample output).
•	The 3 subclasses all have an occursOn method, which accepts a month and day input, 
and returns True / False depending on whether the current appointment object will occur on the input month / day.
'''


class Appointment :
    #constructor
    def __init__(self, month, day, eventname) :
        self._month = month
        self._day = day
        self._eventname = eventname       
    def occursOn(self, date) :
        raise NotImplementedError
    #def __repr__(self) :
        #raise NotImplementedError
    
''' superclass and abstract class, requires month, day and eventname'''
            
class Onetime(Appointment) :  
    def __init__(self, month, day, eventname) :      
        super().__init__(month, day, eventname)      
    def __repr__(self) :
        return "One time appointment (" + "%02d"%self._month + "/" + "%02d"%self._day + "): " + self._eventname
    def occursOn(self,date) :
        if self._month == date[0] and self._day == date[1] :
            return True     ### return false for eslse

'''subclass, print the appointment and test whether the current appointment object will occur on the input date '''
        
class Daily(Appointment) :
    def __init__(self, month, day, eventname) :      
        super().__init__(month, day, eventname)
    def __repr__(self) :
        return "Daily appointment starting (" + "%02d"%self._month + "/" + "%02d"%self._day + "): " + self._eventname   
    def occursOn(self,date) :
        if self._month < date[0] :
            return True
        elif self._month == date[0] and self._day <= date[1] :
            return True
        else :
            return False
    #### return month > self._month or (month == self._month and day >= self._day)
    ### return month > self.month and month == self._month

'''subclass, print the appointment and test whether the current appointment object will occur on the input date '''
    
class Monthly(Appointment) :
    def __init__(self, month, day, eventname) :      
        super().__init__(month, day, eventname)        
    def __repr__(self) :
        return "Monthly appointment starting (" + "%02d"%self._month + "/" + "%02d"%self._day + "): " + self._eventname   
    def occursOn(self,date) :
        if self._month <= date[0] and self._day == date[1] :
            return True     ### return false for eslse

'''subclass, print the appointment and test whether the current appointment object will occur on the input date '''   