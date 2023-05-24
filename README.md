# Homeworker

This is a quick example of how to use a large language model, like ChatGPT with external content.
The data linked below is Great Expectations by Dickens published part of the Gutenberg Project, 
any text data should work.


## Setup

Some necessary setup

* Setup a python environment, I just use virtualenv - whatever rocks your boat, no need for conda on this one
* Clone the source code https://github.com/pjaol/homeworker
* install the requirements pip install -i requirements.txt
* mkdir data
* Download Great Expectations from Project Gutenberg and copy it to your data directory [https://www.gutenberg.org/ebooks/1400](https://www.gutenberg.org/ebooks/1400) (get the text version)
* mkdir settings
* Create an account and get an API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
* Add key to settings/.env
    * OPEN_AI_KEY=XXXXXXX


