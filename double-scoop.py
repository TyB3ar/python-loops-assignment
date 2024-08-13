# Task: Mood Tracker 

# Simulate a mood tracker that tracks your mood 3 times a day (morning, afernoon, evening) for each day of week
# Use nested loops 

import random 

moods = ["Happy", "Sad", "Energetic", "Calm"] 
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# add in the times of day
time_of_day = ["Morning", "Afternoon", "Evening"] 

#squeeze it in to the loop to iterate every day and every time of day
for i in range(7):  
    for time in time_of_day:       # every time of day for each day             
        for mood in moods:         # Still shuffle the moods, but now for each time of day
            random.shuffle(moods)
        print(f"On {week_days[i]} {time} I felt {mood}")     # print it out according to each time of day 

      