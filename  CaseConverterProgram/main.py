def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')
def main():
    pascal_or_camel_cased_string = input('Enter pascal or camel cased string: ')
    print(convert_to_snake_case(pascal_or_camel_cased_string))
main()