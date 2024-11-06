
total_minutes = 0

while True:
    segment = int(input("Segment duration: "))
    
    if segment == 0:
        break
    
    total_minutes += segment

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"Total travel time: {hours}:{minutes:02d} hours")
