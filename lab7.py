# lab 7 test driver

from apptManager import ApptManager

# create todo appointment manager
todo = ApptManager()
# run appointment manager
todo.processChoice()

# Note that after all the hard work you've done
# to create the ApptManager and Appointment classes,
# as the user, I don't have to do much work
# to schedule and check my appointments. Jut 2 lines
# of code!

# That's the beauty of OOP: giving the user an easy-to-use
# interface and let the objects do all the heavy work.
# As a user of your classes, I can then build upon your
# classes to create even more complex abstractions (classes 
# that do even more complex work), the same way that
# you rely on the Python built-in classes to write your 
# own classes.