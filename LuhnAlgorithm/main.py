# This algorithm is a formula to validate a variety of identification numbers
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-':'',' ' : ''}) # Remove dashes and spaces using maketrans its used for string translation