# rates are for per 1000 tokens in dollars
rates = {"davinci": 0.12, "curie": 0.012, "babbage": 0.0024, "ada": 0.0016}

# 1000 tokens equates to roughly 750 words

# USAGE 
# For Training Visit: https://openai.com/api/pricing/

# LATEST MODEL	    TOKEN 	WORDS    USD/1K     TOKENS/$1   TOKEN/$18
# text-davinci-003	1000    750     $0.12       8334        1,50,012
# text-curie-001	1000    750     $0.012      83334       15,00,012
# text-babbage-001	1000    750     $0.0024     4,16,667    75,00,006
# text-ada-001		1000    750     $0.0016     6,25,000    1,12,50,000


# LATEST MODEL	    MAX REQUEST 	WORDS    TRAINING DATA
# text-davinci-003	4,000 tokens	3000     Up to Jun 2021
# text-curie-001	2,048 tokens	1536     Up to Oct 2019
# text-babbage-001	2,048 tokens	1536     Up to Oct 2019
# text-ada-001		2,048 tokens	1536     Up to Oct 2019


















# 1 token is 0.75 words
# word_multiplier = 0.75
# price_multiplier = 0.12

# balance = input("Please enter credit balance: ")
# tokens=int((float(balance)/price_multiplier)*1000)
# print(tokens)
# token=input('Enter number of tokens: ')
# price=(int(token)/1000)*price_multiplier
# print(price)
# words_needed=input('Enter number of words: ')
# tokens=int(float(words_needed) * word_multiplier)
# print(tokens)