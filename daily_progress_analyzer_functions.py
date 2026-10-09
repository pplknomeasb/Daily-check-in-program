#Daily progress analyzer.  using functions to make code simpler


#this function represts all 
def get_valid_number(question, minimum, maximum):
	while True:
		number = int(input(question))
		
		if minimum <= number <= maximum:
			return number
		else:
			print(f"Enter a number that is greater than {minimum} and {maximum}...")
	except ValueError:
		print(f"You have to answer with a number between {minimum} and {maximum}.  No letters and characters...")

def get_valid_yesno(question):
	answer = input(question).strip().lower()
