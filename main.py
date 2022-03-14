print("Welcome to Derek's Github Page!")
print("This first project is a simple tool to help basketball players record their statistics and turn them into percentages that are easy to read.")
total_fga = int(input("Please input your total field goals attempted regardless of make or miss: "))
made_fga = int(input("Please input your total made field goals: "))
totalFga_percent = (made_fga / total_fga) * 100
total_twoPoint = int(input("Out of your total field goal attempts, how many were inside the 3 point line? "))
total_threepoint = total_fga - total_twoPoint
made_threepoint = int(input("Please enter the amount of three point shots you made: "))
threepoint_perc = (made_threepoint / total_threepoint) * 100
made_twopoint = made_fga - made_threepoint
twopoint_perc = (made_twopoint / total_twoPoint) * 100
fta = int(input("Please enter the amount of free throws you attempted: "))
ftm = int(input("Please enter the amount of free thrwos you made: "))
ft_perc = (ftm/ fta) * 100
print("Your shot summary is: ")
print("Total made field goal percentage: ", totalFga_percent, '%')
print("Made two point percentage: ", twopoint_perc, "%")
print("Made three point percentage: ", threepoint_perc, "%")
print("Made free throw percentage: ", ft_perc, "%" )
if totalFga_percent < 40:
    print("You're struggling overall from the field, try to get this number to above 40%,")
elif totalFga_percent >= 40 and totalFga_percent <= 45:
    print("Your total field goal percentage is on par with a divison 1 basketball player.")
else:
    print("Your total field goal percentage is exceptional!")
if ft_perc < 70:
    print("You're struggling with your free throws, try to get this above 70%.")
elif ft_perc >= 70 and ft_perc <= 85:
    print("Your free throw percentage is on par with a divison 1 basketball player!")
else:
    print("Your free throw percentage is on par with a professional basketball player!")




