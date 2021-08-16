# [10 Real World Apps](https://www.udemy.com/course/the-python-mega-course/)
My code along repo and all associated projects

### 01 English Thesaurus
This project contains 2 versions of a simple english thesaurus:
1. `thesaurus_json_data.py` reads data from a `data/data.json` file to return definitions of user entered words
2. `thesaurus_db_data.py` connects to a `Dictionary` database to return definitions of user entered words

The `thesaurus_json_data.py` version has some additional features such as:
- Finding close but not exact match words
- Prompting the user to confirm if that is what was meant
- Looping through close match options till one is confirmed, or all are exhasted

Bother versions handle differences in word capitalization by converting the user input into lowercase
