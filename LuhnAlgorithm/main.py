# This algorithm is a formula to validate a variety of identification numbers
# The Luhn algorithm is as follows:
#
# From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
# Take the sum of all the digits.
# If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]  # Reverse the string
    odd_digits = card_number_reversed[::2]  # Get the odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)  # Add the odd digit

    even_digits = card_number_reversed[1::2]
    sum_of_even_digits = 0  # Get the even digits
    for digit in even_digits:
        number = int(digit) * 2  # Double the even digit
        if number > 9:
            number = number % 10 + number // 10  # If the product is greater than 9, sum the digits of the products
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0


def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans(
        {'-': '', ' ': ''})  # Remove dashes and spaces using maketrans its used for string translation
    translated_card_number = card_number.translate(card_translation)  # Translate the card number
    if verify_card_number(translated_card_number):
        print('The card number is valid')
    else:
        print('The card number is not valid')
    verify_card_number(translated_card_number)


main()
