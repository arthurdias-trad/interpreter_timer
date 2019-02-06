from datetime import datetime as dt, timedelta as td

# Get interpreter names
first_terp = input("Interpreter 1: ")
second_terp =  input("Interpreter 2: ")

# Get start and end times
start_time_string = input("Enter starting time (HH:MM, 24-h format): ")
end_time_string = input("Enter starting time (HH:MM, 24-h format): ")

# Create start and end times datetime objects
start_time = dt.strptime(start_time_string, "%H:%M")
end_time = dt.strptime(end_time_string, "%H:%M")

# Get block size
block_string = input("Enter the time until turnover (in minutes): ")

# Create timedelta object
block = td(minutes=int(block_string))

# Create loops to print out interpreter's turns
count = 0
while start_time < end_time:
    if count % 2 == 0:
        terp = first_terp
    else:
        terp = second_terp
    
    if (end_time - start_time) < block:
        temp =  start_time + (end_time - start_time)
    else:
        temp = start_time + block
    print("{}: {} - {}".format(terp, start_time.strftime("%H:%M"), temp.strftime("%H:%M")))
    start_time = temp
    count += 1

input("Press any key to exit")
