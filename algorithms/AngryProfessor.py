# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (arrivalTime<=0) to arrived late (arrivalTime>=0).

# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

# Example
# n = 5
# k = 3
# a = [-2,-1,0,1,2]

# The first 3 students arrived on. The last 2 were late. The threshold is 3 students, so class will go on. Return YES.

# Note: Non-positive arrival times (a[i]<=0) indicate the student arrived early or on time; positive arrival times (a[i]>0) indicate the student arrived a[i] minutes late.

# Function Description

# Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

# angryProfessor has the following parameter(s):

# int k: the threshold number of students
# int a[n]: the arrival times of the  students
# Returns

# string: either YES or NO
def angryProfessor(k, a):
    # Initialize a counter for students who are on time
    on_time_count = 0
    
    # Iterate through the arrival times to count students who are on time
    for time in a:
        if time <= 0:
            on_time_count += 1
            
    # Check the threshold and return the result
    if on_time_count >= k:
        return "NO"  # Class will go on
    else:
        return "YES"  # Class is canceled

# Example usage
n = 5
k = 3
a = [-2, -1, 0, 1, 2]
result = angryProfessor(k, a)
print(result)  # Output will be "NO"
