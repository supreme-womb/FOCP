#program that stimulates a Bridge-keeper charged with guarding an important bridge
name = input("What is your name? ")
if name.lower() != "aurthur":
    seek = input("What do you seek? ")
    if "grail" in seek.lower():
        color = input("What is your favourite color? ")
        if color[0].lower()==name[0].lower():
            print("You may enter my Knight")
        else:
            print("Entry is denied")
    else:
        print("Entry is denied")  
else:
    print("You may pass my king")
        