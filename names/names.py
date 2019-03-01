import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# This looks like a runtime complexity of O(n ** 2) because of the nested for loop.
duplicates = []
# for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

# This one takes about 2 seconds to run
# for name_1 in names_1:
#    if name_1 in names_2:
#        duplicates.append(name_1)

# Trying an attempt using sets - runtime = 0.005786895751953125 seconds
set_1 = set(names_1)
set_2 = set(names_2)

duplicates.append(str(set_1 & set_2))

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
