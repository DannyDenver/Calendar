"""
This is a command line calendar. You can view, add events, delete events and update events.
"""

from time import sleep, strftime

USER_FIRST_NAME= "Danny"

calendar={}

def welcome():
  print "Welcome, "+ USER_FIRST_NAME+"."
  print "Loading..."
  sleep(1)
  print "Today is "+strftime("%A %B %d,%Y")
  print strftime("%H: %M: $S")
  sleep(1)
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start=True
  while start:
    user_choice= raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:. Store their input in a variable called")
    user_choice.upper()
    if user_choice=="V":
      if len(calendar.keys())<1:
        print "The calendar is empty. "
      else:
          print calendar
    elif user_choice=="U":
			date=raw_input("What date?")
			update=raw_input("Enter the update: ")
			calendar[date]=update
			print "Update made."
			print calendar
    elif user_choice=="A":
    	event=raw_input("Enter event: ")
      date=raw_input("Enter date (MM/DD/YYYY)")
      	if (len(date)>10 or int(date[6:])<int(strftime("%Y"))):
        	print "Incorrect format. Must be (MM/DD/YYYY) at future date."
          try_again= raw_input("Try again? Y for Yes, N for No: ")	
          try_again.upper()
             if try_again=="Y":
             		continue
             else:
             		start=False
				else:
          calendar[date]=event
         	print "Event successfully added."
          print calendar
		elif user_input=="D":
       if len(calendar.keys())<0:
             print "Calendar is empty"
   else: 
             event=raw_input("What event?")
             		for date in calendar.keys():
             			if event==calendar[date]:
             				del calendar[date]
            				print "Event deleted successfully"
             				print calendar
             			else: 
             print "Incorrect event was specified"
		elif user_input=="X":
   		start=False
    else:
      print "Invalid command was entered."
      exit()
start_calendar()
             
       
             
             
            
             
       
      
