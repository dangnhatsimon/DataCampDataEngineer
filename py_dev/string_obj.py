# Create review_one
review_one = """
    I really enjoy the courses,
    and they are easy to fit into my busy schedule. 
    I wish I had started using your platform sooner.
    I'll be recommending you to my friends!!
"""

# Create review_two
review_two = """
    One year ago, I was unsure of how to make progress in my career. 
    Now, I work as a Prompt Engineer, and I can't thank you enough! 
    Keep up the great work.
"""

# Print the two reviews individually
print(review_one)
print(review_two)


most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ", "_")

# Change to lowercase
most_popular_course = most_popular_course.lower()

print(most_popular_course)