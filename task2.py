#Speed Analysis of shallow birds
Kph = []
c=0
print("*****SHALLOW SPEED ANALYSIS*****")
while True:
    c+=1
    initial_speed = input("Enter the speed Reading: ")
    if initial_speed != "":
        try:
            speed = float(initial_speed[1:])
            if initial_speed[0] == "E":
                speed = float(initial_speed[1:])
                Kph.append(speed)
            elif initial_speed[0] == "U":
                speed = float(initial_speed[1:])
                Kph.append(speed*1.60934)
            else:
                print("Enter the reading in right format. ")
        except:
            print("Wrong Format of Input! Try entering the speed in right format.")
    else:
        print("No input was provided!")
        break

print(Kph)
print("{} Readings Analyzed.".format(c-1))
print("Max Speed:     {:.2f} KPH, {:.2f} MPH ".format(max(Kph), max(Kph)*0.621371))
print("Min Speed:     {:.2f} KPH, {:.2f} MPH ".format(min(Kph), min(Kph)*0.621371))
print("Average Speed: {:.2f} KPH, {:.2f} MPH ".format(sum(Kph)/len(Kph),sum(Kph)/len(Kph)*0.621371))
