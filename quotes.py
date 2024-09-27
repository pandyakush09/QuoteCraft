import json
import random 

f = open('quotes.json')

quotes_dict = json.load(f)
all_the_quotes = list(quotes_dict["quotes_list"])



def getRandomQuote(quotes_list):
    random_num = random.randint(0, 5)
    quote_obj = quotes_list[random_num]
    return quote_obj 


def printQuote():
    random_quote = getRandomQuote(all_the_quotes)

    return random_quote 


f.close()