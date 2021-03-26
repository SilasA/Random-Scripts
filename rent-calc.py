#!/usr/bin/python3

# Store rent in cents
print("Enter total rent: $", end="")
rent = int(float(input()) * 100)

print("Enter total sqft: ", end="")
total_area = int(input())

print("Enter the number of residents: ", end="")
num_beds = int(input())

beds = []
bed_area = 0

for i in range(num_beds):
    print("Enter name and bedroom sqft: ", end="")
    beds.append(str(input()).split())
    beds[i][1] = int(beds[i][1])
    bed_area += beds[i][1]

# Bedroom factorable rent in cents
factorable_rent = round(bed_area / total_area * rent)
rem_rent_split = (rent - factorable_rent) / 4

# Compute rent per room
for bed in beds:
    bed.append(round(bed[1] / bed_area * factorable_rent) + rem_rent_split)
    print

# Display
print("\n------------------------------------------------------------------")
print("Total Rent: " + str(float(rent / 100)))
print("Bedroom Rent: " + str(float(factorable_rent / 100)))
for bed in beds:
    print("\t" + bed[0] + ": " + str(float(bed[2] / 100)))
