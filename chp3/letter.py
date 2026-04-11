letter = """
Dear (Applicant), We are pleased to inform you that you are called for interview on (Date)


"""

print(letter.replace("(Applicant)" , "Joey Tribbiani").replace("(Date)", "15 December 2027") )

# this is chaining, first we replaced app-> joey then on that string we repalced date -> 15 december 2027....

#also .replace does not create a new string, it just returns a new string with the changes, the original string remains unchanged.


print(letter) # this will print the original letter without any changes.