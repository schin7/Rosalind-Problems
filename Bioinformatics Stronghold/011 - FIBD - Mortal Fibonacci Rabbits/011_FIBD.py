with open('C:/Users/Owner/Desktop/rosalind_fibd.txt') as input_data:
    n,m = map(int, input_data.read().split())

# Populate the initial rabbits.
Rabbits = [1]+[0]*(m-1)

# Calculate the new rabbits (bunnies), in a given year.
# Start at use range(1,n) since our initial population is year 0.
for year in range(1, n):
    Bunnies = 0
    # Get the number of Rabbits able to old enough to give birth.
    for j in range(1,m):
        Bunnies += Rabbits[(year-j-1)%m]
    # Bunnies replace the old rabbits who died.
    Rabbits[(year)%m] = Bunnies

# Total rabbits is the sum of the living rabbits.
Total_Rabbits = sum(Rabbits)

# Write the output data.
with open('C:/Users/Owner/Desktop/011_FIBD.txt', 'w') as output_data: 
    print (Total_Rabbits)
output_data.write(str(Total_Rabbits))


if __name__ == '__main__':
    main()