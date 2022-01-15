import pikanam
import get_name
import pikanam
import to_lower

network = list(range(0,9))
end = ["bye","exit","close"]
operator_names = ['Martha','Stewart', 'Jane', 'Paula', 'Lacy', 'Samantha', 'David', 'Marilyn', 'Elizabeth']
phases = ["Hmm","Oh! I See!","Tell me More","Is that All?"]

print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")

email = input("Please enter your Poppleton email address:")

print(f"Hi, {get_name.first_name(email)}! Thank you, and Welcome to PopChat!")
print(f"My name is {pikanam.choose(operator_names)}, and it will be my pleasure to help you. ")

while True:
    querry = input("---->")
    q = to_lower.to_lowercase(querry)
    if pikanam.choose(network) == 0:
        print("Network Error!")
        break
    if q in end:
        break
    elif q == "wifi":
        print("Wifi is excellent across the campus. ")
    elif q == "library":
        print("The library is closed today. ")
    elif q == "deadline":
        print("Your deadline has been extended by two working days. ")
    elif q == "classes":
        print("The classes are being conducted as per the schedule. ")
    elif q == "fees":
        print("Your pending balance is Nil! ")
    else:
        print(pikanam.choose(phases))