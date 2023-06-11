import lexer
from parser_eta import parser
import sys

def process_input(input_text):
    lexer.lexer.input(input_text)
    result = parser.parse(input_text)
    print(result)

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            process_input(file_contents)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def open_console():
    print("Eta Console")
    print("Enter 'exit' to quit.")

    while True:
        user_input = input("> ")

        if user_input == 'exit':
            break

        if user_input.startswith("open "):
            file_path = user_input[5:]  # Remove the 'open ' prefix
            process_file(file_path)
        else:
            process_input(user_input)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        process_file(file_path)
    else:
        open_console()
