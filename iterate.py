__author__ = 'PRASHANT'

# movies = ["Gladiator","Terminator","x-Men"]
movies = [
"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman",
["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

# using for to iterate over list

for each_movie in movies:
    print(each_movie)

# using while loop to iterate over list

count=0
while(count< len(movies)):
    print(movies[count])
    count = count +1



# using list inside list


print(movies[4][1][3]) # will print Eric Idle




