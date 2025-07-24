# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need


import string
import random
import re

def generate_shortcode(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def is_valid_url(url):
    pattern = re.compile(
        r'^(https?://)'   
        r'([\w\-]+\.)+[\w\-]+'  
        r'(:\d+)?'        
        r'(/[^\s]*)?'      
        r'$',
        re.IGNORECASE
    )
    return bool(pattern.match(url))
