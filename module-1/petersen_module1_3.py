# Monika Petersen
# CSD325
# Module 1.3
# 6/14/2026

#Loop to go through the song until bottles are gone
def song(bottles):
    for i in range(bottles, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        if i > 0:
            print(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.\n")

# Get user input, then go to song function to loop through the song until there are no more bottles left
num_bottles = int(input("Enter number of bottles: "))
song(num_bottles)
print("Time to buy more bottles of beer.")