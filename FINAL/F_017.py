# Given regression parameters
intercept = 20.71
coefficient_tickets_sold = 0.7162

y_goal = 250  # Goal for boxes of popcorn

# Calculate the number of movie tickets needed
x_needed = (y_goal - intercept) / coefficient_tickets_sold

# Excel output format
print(f"=({y_goal} - {intercept}) / {coefficient_tickets_sold}")