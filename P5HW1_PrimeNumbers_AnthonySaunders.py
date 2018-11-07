#Determining prime numbers
#11-5-2018
#CTI - 110 Prime numbers
#Anthony Saunders

# Set up function for is_prime

def is_prime(user_number):

    even_division = 0

    if user_number == 1:
        return False
# Set range for user number to be tested for prime status
    for this_number in range( 1, user_number +1):
        if user_number % this_number == 0:
            even_division = even_division + 1
            if even_division > 2:
                return False

    return True
# Set up main function
def main():
    # Set range for prime number to go up to
    for this_number in range(1, 101):
        if is_prime(this_number):
            # Display prime numbers
            print("Prime numbers from 1 to 100 are:" ,this_number)

            

    
    


main()

    
