# Activity Selection Problem

def activity_selection(start, finish):
    n = len(start)
    activities = []
    
    # Step 1: Combine start and finish times into activities
    for i in range(n):
        activities.append((start[i], finish[i], i))
    
    # Step 2: Sort activities based on finish times
    activities.sort(key=lambda x: x[1])
    
    # Step 3: Select compatible activities
    selected_activities = [activities[0]]
    for i in range(1, n):
        if activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(activities[i])
    
    # Step 4: Print selected activities
    print("Selected Activities:")
    for activity in selected_activities:
        print(f"Activity {activity[2]} (start time: {activity[0]}, finish time: {activity[1]})")

# Example Usage:
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]
activity_selection(start_times, finish_times)

