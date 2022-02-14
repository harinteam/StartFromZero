
"""
# repeat = 10

# for i in range(repeat):
   # print(f"repeated - {i}")

"""

"""
answer = 'yes'
count = 0

while(True):
    count += 1
    answer = input("want to repeat?? ")
    if answer == 'no':
        break

print(f"Total repeated: {count}")
"""

answer = 'yes'
count = 0

while (answer == 'yes'):
    count += 1
    answer = input("want to repeat?? ")

print(f"Total iterations: {count}")