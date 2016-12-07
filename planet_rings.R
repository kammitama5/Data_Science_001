# The planets_df data frame from the previous exercise is pre-loaded
planets_df[1, 3]
# Print out diameter of Mercury (row 1, column 3)
print(planets_df[1,3])

# Print out data for Mars (entire fourth row)
print(planets_df[4, ])


# planets_df is pre-loaded in your workspace

# Select the rings variable from planets_df
rings_vector <- planets_df$rings
  
# Print out rings_vector
rings_vector

# planets_df and rings_vector are pre-loaded in your workspace

# Adapt the code to select all columns for planets with rings
planets_df[rings_vector, ]