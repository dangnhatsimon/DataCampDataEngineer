# Find out more about lists
print(help(list))

# Find out more about int
print(help(int))

# Find out more about len()
print(help(len))


course_ratings = {"LLM Concepts": 4.7, 
                  "Introduction to Data Pipelines": 4.75, 
                  "AI Ethics": 4.62, 
                  "Introduction to dbt": 4.81}

# Print the number of key-value pairs
num_courses = len(course_ratings)
print(num_courses)

course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

# Find the number of courses
num_courses = len(course_completions)
print(num_courses)

most_popular_course = "Introduction to dbt"

# How many characters are in most_popular_course?
title_length = len(most_popular_course)
print(title_length)


# Print the total number of course completions
print(sum(course_completions))

# Print the largest number of completions
print(max(course_completions))

# Print the average number of completions
print(sum(course_completions) / len(course_completions))

# Print the average number of completions, rounded to one decimal places
print(round(sum(course_completions) / len(course_completions), 1))