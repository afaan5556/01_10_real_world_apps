from difflib import get_close_matches
from logging import basicConfig
import mysql.connector
import configparser
import logging


def query_db(user_name, password, host, data_base):
    '''
    user_name: The username for the DB
    password: The password for the DB
    host: The host name for the DB
    data_base: The DB name
    return: The queried results
    '''
    userInput = input('Enter word: ')
    userLowerInput = userInput.lower()
    con = mysql.connector.connect(
        user=user_name,
        password=password,
        host=host,
        database=data_base
        )

    cursor = con.cursor()
    query = "SELECT * FROM Dictionary WHERE Expression = '{}'".format(userLowerInput)
    cursor.execute(query)
    results = cursor.fetchall()

    return results


def main():
    basicConfig(level=logging.INFO, format="%(asctime)s\t%(levelname)s\t%(message)s")

    # Parsing Config File
    config = configparser.ConfigParser()
    config.read('config.ini')
    USER_NAME = config['CREDS']['UserName']
    PASSWORD = config['CREDS']['Password']
    HOST = config['CREDS']['Host']
    DATA_BASE = config['CREDS']['DataBase']

    # Getting user input and appropriate response
    appropriateResponse = query_db(USER_NAME, PASSWORD, HOST, DATA_BASE)

    # Printing results or message
    if not appropriateResponse:
        print("No such word found")
    else:
        for i in appropriateResponse:
            print(i[1])


if __name__ == '__main__':
    main()
