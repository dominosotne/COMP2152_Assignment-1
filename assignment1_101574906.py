"""
Author:  Alikhan Zhilkibayev
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# Step c: Create a dictionary named workout_stats
# Dictionary: keys are friend names, values are tuples of workout minutes.
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 30),
    "Taylor": (25, 50, 45),
    "Morgan": (20, 30, 35),
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
friends = list(workout_stats.keys())
for friend in friends:
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
# 2D list: rows are friends, columns are activities.
workout_list = [list(workout_stats[friend]) for friend in friends]

# Step f: Slice the workout_list
yoga_running_minutes = [row[:2] for row in workout_list]
print("Yoga and running minutes for all friends:", yoga_running_minutes)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for the last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120
for friend in friends:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name: ").strip()
if friend_name in friends:
    minutes = workout_stats[friend_name]
    total = workout_stats[f"{friend_name}_Total"]
    print(
        f"{friend_name}'s workout minutes - "
        f"Yoga: {minutes[0]}, Running: {minutes[1]}, "
        f"Weightlifting: {minutes[2]}, Total: {total}"
    )
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {friend: workout_stats[f"{friend}_Total"] for friend in friends}
highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)
print(
    f"Highest total workout minutes: {highest_friend} "
    f"({totals[highest_friend]})"
)
print(
    f"Lowest total workout minutes: {lowest_friend} "
    f"({totals[lowest_friend]})"
)