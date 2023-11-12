text = 'Our competitor pricing is $10.50 an inch. Our price is $125.00 a foot.'

import re
import math

def extract_0(text):
    # match and extract dollar amounts from the text
    return re.findall(r'\$\d+\.\d\d', text)

def extract_1(text):
    # return all matches to regex pattern
    return re.findall(r'\$\d+\.\d\d', text)

# Print the text
print(text)

# Print the results of the function with better commenting
print(extract_0(text))


def goldilocks(bear):
    """_summary_

    :param bear: which number bear's food are you trying to eat; valid numbers: [1, 2, 3]
    :return: description of how the food's temperature is
        
    >>> goldilocks(bear=1)
    'too hot'
    """
    pass

def rapunzel(hair_len):
    """_summary_

    :param hair_len: length of hair (cannot be negative)
    :return: strand of hair that is hair_len characters long
        
    >>> rapunzel(hair_len=15)
    '~~~~~~~~~~~~~~~'
    """
    
def mary(white_as):
    """_summary_

    How white was mary's little lamb?
        
    >>> mary(white_as='salt')
    'Mary had a little lamb whose fleece was white as salt'
    """
    pass

def sleeping_beauty(awake):
    """_summary_

    Should Sleeping Beauty wake up?
        
    :param awake: if True then wake up; else snooze
    :return: string showing sleepiness or wakefulness
    
    ~~~~~~~~~~~~~~~~~~~~
    """
    pass

# Run the help on all 4 functions
help(goldilocks)
help(rapunzel)
help(mary)
help(sleeping_beauty)

# Execute the function with most complete docstring
result = rapunzel()

# Print the result
print(result)



# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall 
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ['the', 'rain', 'in', 'spain']
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize)




def hypotenuse_length(leg_a, leg_b):
    """Find the length of a right triangle's hypotenuse

    :param leg_a: length of one leg of triangle
    :param leg_b: length of other leg of triangle
    :return: length of hypotenuse
    
    >>> hypotenuse_length(3, 4)
    5
    """
    return math.sqrt(leg_a**2 + leg_b**2)


# Print the length of the hypotenuse with legs 6 & 8
print(hypotenuse_length(6,8))


from statistics import mean

# Sample measurements of pupil diameter in mm
pupil_diameter = [3.3, 6.8, 7.0, 5.4, 2.7]

# Average pupil diameter from sample
mean_diameter = mean(pupil_diameter)

print(mean_diameter)



def polygon_perimeter(n_sides, side_len):
    return n_sides * side_len

def polygon_apothem(n_sides, side_len):
    denominator = 2 * math.tan(math.pi / n_sides)
    return side_len / denominator

def polygon_area(n_sides, side_len):
    """Find the area of a regular polygon

    :param n_sides: number of sides
    :param side_len: length of polygon sides
    :return: area of polygon

    >>> round(polygon_area(4, 5))
    25
    """
    perimeter = polygon_perimeter(n_sides, side_len)
    apothem = polygon_apothem(n_sides, side_len)

    return perimeter * apothem / 2

# Print the area of a hexagon with legs of size 10
print(polygon_area(n_sides=6, side_len=10))





from text_analyzer import Document

class SocialMedia(Document):
    """Analyze text data from social media
    
    :param text: social media text to analyze

    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
