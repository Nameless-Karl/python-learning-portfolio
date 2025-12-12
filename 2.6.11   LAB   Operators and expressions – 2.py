hours = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
# if  hours != 0
t_mins = hours * 60
duration = t_mins + mins + dura
t_hours = duration//60
t_duration = duration %60

print("Event started at: ", hours,":",mins,"\nLasted: ", dura," minutes","\n\nEnds at: ", t_hours,":",t_duration)
