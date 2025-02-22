#tuple object is collection of ordered items and unchaneable
#tuple()
temp_string =[ "swetha","teja","prathima"]
print (temp_string)
print (tuple(temp_string))
#list()
list(temp_string)
temp_string.append("sasi")
temp_string = tuple(temp_string)
print (temp_string[1])
print (temp_string[-1])
#0,1,2,3
   #0       1      2     3      4
#[ sasi, prathima,teja, surya, swetha]
#     -4     -3     -2    -1
#('swetha', 'teja', 'prathima', 'sasi')
#remove(temp_string)
temp_string = list(temp_string)

temp_string.remove('sasi')

temp_string = tuple(temp_string)

print(temp_string)
temp_string = list(temp_string)
temp_string.append("sasi")
temp_string.append("saadakjdhsi")
temp_string.append("asdjklasd")
temp_string = tuple(temp_string)
#('swetha', 'teja', 'prathima', 'sasi',adakjdh,dasdljaldsj,asdjklasd)
(pizza,*biryani,sambar) = temp_string

print(pizza,sambar,*biryani, sep=",")

# loop 

# for i in range(0,len(temp_string),):
#     print(temp_string[i])

# for i in temp_string:
#     print(i)
i = 0
while i < len(temp_string):

    print(temp_string[i])
    i += 1


#join tuple
tuple1 = ("sasi","surya","teja","prathima","swetha")
tuple2 = ("p","y","c","m")

new_tuple = tuple1 + tuple2
print(new_tuple)

#multiply tuple
new_tuple = tuple1*2
print(new_tuple)
#count()
print(new_tuple.count("sasi"))


