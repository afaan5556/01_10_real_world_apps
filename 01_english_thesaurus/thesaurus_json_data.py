from difflib import get_close_matches
from logging import basicConfig
import configparser
import logging
import json


def read_json_data(full_data_path):
    '''
    Read json data and return object
    full_data_path: The path to the json data file
    return: The json object of english dictionary data
    '''
    return json.load(open(full_data_path))


def get_response(english_thesaurus_data, close_match_cutoff, close_match_count):
    '''
    Get user input and check json data for an exact or close match
    Send responses, user prompts, or error messages accordingly
    english_thesaurus_data: The json object of english dictionary data
    close_match_cutoff: The value at which to cut-off match determined as close
    close_match_count: The number of close matches to use
    return: Either the exact match, close match, or appropriate error message
    '''
    userInput = input('Enter word: ')
    userLowerInput = userInput.lower()
    # Case 1: Lower case match found
    if userLowerInput in english_thesaurus_data.keys():
        return english_thesaurus_data[userLowerInput]

    # Case 2: Close word match found in lower case
    if not get_close_matches(userLowerInput, english_thesaurus_data.keys(), close_match_count, close_match_cutoff):
        return 'No such word found. Please check entry'
    else:
        for i in get_close_matches(userLowerInput, english_thesaurus_data.keys(), close_match_count, close_match_cutoff):
            while True:
                userPromptResponse = input('Did you mean {}? Enter Y or N: '.format(i))
                if userPromptResponse.lower() == 'y':
                    return english_thesaurus_data[i]
                elif userPromptResponse.lower() == 'n':
                    break
                else:
                    print('Invald response. Please enter either Y or N: ')

    # Case 3: No match found
    return 'No such word found. Please check entry'


def main():
    basicConfig(level=logging.INFO, format="%(asctime)s\t%(levelname)s\t%(message)s")

    # Parsing Config File
    config = configparser.ConfigParser()
    config.read('config.ini')
    DATA_FOLDER_PATH = config['FILE_PATHS']['Data']
    ENGLISH_THESAURUS_DATA = config['FILE_NAMES']['EnglishThesaurusData']
    CLOSE_MATCH_CUTOFF = float(config['CONSTANTS']['CloseMatchCutoff'])
    CLOSE_MATCH_COUNT = int(config['CONSTANTS']['CloseMatchCount'])

    # Loading json file
    englishThesaurusData = read_json_data(DATA_FOLDER_PATH + ENGLISH_THESAURUS_DATA)

    # Getting user input and appropriate response
    appropriateResponse = get_response(englishThesaurusData, CLOSE_MATCH_CUTOFF, CLOSE_MATCH_COUNT)

    # Printing results or message
    if isinstance(appropriateResponse, str):
        print(appropriateResponse)
    else:
        for i in appropriateResponse:
            print(i)


if __name__ == '__main__':
    main()
