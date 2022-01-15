def isemail(email):
    if '@' in email:
        return True
    else:
        return False

def isvalid(email):
    if len(email.split('@')[0]>2):
        return True
    else:
        return False

def ispoppleton(email):
    if email.split('@')[1] == "pop.ac.uk":
        return True
    else:
        return False

def first_name(email):
    name = email.split('@')[0]
    return name

