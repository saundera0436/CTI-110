#Adding number of bugs for 5 days
#CTI - 110 - P4T2 - Bug Collector
#10-17-2018
#Anthony Saunders

#Initialize the accumulator
total = 0
# Get the bugs collected for each day
for day in range(1, 6):
    print("Enter the number of bugs collected on day", day)
    bugs = int(input())
    total = total + bugs

#Display the total bugs
print("You have collected a total of", total, "bugs.")
