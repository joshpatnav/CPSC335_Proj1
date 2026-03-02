from typing import List

def algo1(row):
    # Initialize the vairables
    seat1 = 0
    seat2 = 0
    numswaps = 0
    m = len(row)  

    # Create the positional mapping
    pos = [0] * m     
    for i, p in enumerate(row):
        pos[p] = i

    # Process through the pair
    for i in range(0, m, 2):
        # Find seat1
        seat1 = row[i]
        # Find the supposed couple for seat1
        if (seat1 % 2) == 0:
            seat2 = seat1 + 1
        else:
            seat2 = seat1 - 1
        # If they aren't equal then swap
        if row[i+1] != seat2:
            numswaps += 1 # Increment num swaps

            # Swapping positions
            position = pos[seat2]
            temp = row[i+1]
            row[i+1] = seat2
            row[position] = temp

            # Updating the positions
            pos[seat2] = i + 1
            pos[temp] = position

    print(row) # Check if they actually swap
    return numswaps

# Example 1 
row1 = [0, 2, 1, 3]
print(algo1(row1))
# Example 2
row2 = [5, 2, 1, 3, 0, 4]
print(algo1(row2))