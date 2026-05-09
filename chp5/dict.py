
# key value pairs

marks={

"Ali" : 90,
"Ozan"  : 80,
"Ahmet" : 70,
"Celal" : 60,
"previous_topers" : [99,89,88],
"Celal" : 99 # duplicate keys not allowed, so previous will be overwritten



}


# print(marks,type(marks))

# print(marks["Ozan"])
# print(marks["previous_topers"])

# print(marks["Celal"])

# print(marks.keys()) -- only all keys
# print(marks.values())   --all values

# print(marks.items()) #all key value pairs


marks.update({"Celal" : 100,"Ayush":77}) 
#celal updated , ayush added

print(marks)