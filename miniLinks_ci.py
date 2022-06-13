import db_script
import string
import random
import validators
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv('DB_PASSSWORD')
DOMAIN = os.getenv('DOMAIN')
MAX_CODE_LENGTH = int(os.getenv('MAX_CODE_LENGTH'))

def get_code(db):
    letters = string.ascii_lowercase
    unique = False
    while not unique:
        code = ''.join(random.choice(letters) for _ in range(MAX_CODE_LENGTH))
        if db_script.find_link(db, code, "short") is None:
            unique = True
    return code

def valid_link(link):
    return validators.url(link)

def main():
    client, db = db_script.connect_db(DB_PASSWORD)

    print("Welcome to MiniLinks!")
    response = ""
    while response != "q":
        link = input('Enter a link to shorten: ')
        if not valid_link(link):
            print("Invalid Link. Try again")
            continue

        #create short url
        custom_res = input("Would you like to enter a custom url code? (Ex: domain.com/yourCode)\nEnter Y/N: ")
        if custom_res == "N":
            code = get_code(db)
        else:
            unique = False
            while not unique:
                code = input("Enter link code: ")
                if db_script.find_link(db, code, "short") is None:
                    unique = True
                else:
                    print("Code already exists. Try again. ")

        #short_link found

        link_id = db_script.insert_link(db, link, code)
        if link_id:
            print("Link successfully created")
            short_link = DOMAIN + "/" + code
            print(short_link)

            if input("Shorten another link? (Y/N): ") == "N":
                response = "q"
        else:
            if input("Error. Try again (Y) or Quit (Q): ") == "Q":
                response = "q"
    client.close()

if __name__== "__main__":
    main()