# Task: Today's Mood
# Print out different moods for each day of the week 
import random 

moods = ["Happy", "Sad", "Energetic", "Calm"] 
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for i in range(7):       # Sets the range to loop through each day of the week 
    for mood in moods:   # shuffle the mood for every day
        random.shuffle(moods)
    print(f"Today is {week_days[i]} and I'm feeling {mood}")   # Prints through week_days list in range of 7(days of week) and adds shuffled mood
    
