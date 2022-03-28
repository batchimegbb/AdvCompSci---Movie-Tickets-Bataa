"""
Summative Project: Movie Theatre Ticketing System 
Batchimeg Bumbayar
Advanced Computer Science 
"""

def Ticket_System():
  print("Hello there! It is BB's cinema. How may I help you today?")
  print("--------------------")
  print()

#ask for customers full name and phone number
name = input("Please enter your full name: ")
phone_number = input("Please enter your phone number: ")

#movies available in BB's cinema 
movies = ["Fast and Furious", "Flash", "Titanic"]

print("Movies screening today.")
print("--------------------")
for count, movie in enumerate(movies):
  print(f"{count+1}. {movie}")
movie_choice = None
while movie_choice not in movies:
  movie_choice = input ("Please pick the movie you want to watch: ")

#movie time availability 
available_time = ["Morning", "Afternoon", "Evening"]
choose_time = None
while choose_time not in available_time:
  choose_time = input(f"Please choose the time suitable for you to watch (movie_choice). Morning, afternoon, or in the evening: ")
print(f"{name}, {phone_number}, {movie_choice}, {choose_time}")

#movie seat choices 
available_seats = ["1", "3", "5", "7", "9", "11"]
print(available_seats)
def seats(seat):
    seat = seat.lower()
    match seat:
        case"1":
            return 0
        case"3":
            return 1
        case"5":
            return 2
        case"7": 
            return 3
        case"9":
            return 4 
        case"11":
            return 5
        case _:
            return "Invalid seat"

seat = input("These seats are available, which seat would you like to choose? ")
if (seats(seat)) == "Invalid seat":
    while (seats(seat)) == "Invalid seat":
        seat = input("These seats are available, which seat would you like to choose? ")
        if (seats(seat)) !="Invalid seat":
            available_seats[seats[seat]] = "(X)"
            break
        else:
            print(" ")
            print("Error, your seat is not available.")
            print(" ")
            print(available_seats)
            seat = input("These seats are available, which seat would you like to choose? ")
            print(" ")

available_seats[seats(seat)] = "(X)"
print(available_seats)

book_again = True 

while book_again:
  Ticket_System()
  #customer's final decision
  answer = ''
  while answer not in ("yes", "no"):
    answer = input("Is the information correct? ")
    answer = answer.lower()

if answer == "yes":
  print("Thank you for choosing BB's cinema! Your ticket has been booked")
  book_again = False 
else: 
  #customer's final decision 
  answer = ''
  while answer not in ("yes", "no"):
    answer = input("Do you want to book your movie ticket again?")
    answer = answer.lower()

  if answer == "yes":
    book_again = True
  else:
    book_again = False 
    print("Thank you for choosing BB's cinema! We hope you have a wonderful day today!")


    
