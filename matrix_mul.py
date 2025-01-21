import pandas as pd
import numpy as np

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Loop through each row in the Prices matrix
for i in range(len(Prices)):
    row_sum = 0  # Initialize sum for the current row
    
    # Loop through each price in the current row
    for j in range(len(Prices[i])):
        # Multiply the price by the corresponding quantity in Array2
        row_sum += Prices[i][j] * Array2[i]
    
    # Append the calculated sum for the current row to the Ans list
    Ans.append(row_sum)

# Output the total costs for each row
print(Ans)
