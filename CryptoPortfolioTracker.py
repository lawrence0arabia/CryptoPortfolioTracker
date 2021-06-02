import requests
import time


# PORTFOLIOS 


keanu = {"ETH":55,"DOGE":2323,"MATIC":12496.98,"ADA":200,
         "BEPRO":78118.46,"VET":3736.49,"CWS":34.18,
         "XLM":574,"FVT":7204,"DOT":7,"SYLO":21075,
         "CRO":743,"COMP":0.01212138,"CGLD":1.49,
         "BSV":0.01,"GRT":4.95,"NU":5.73,"AMPL":0.069}

obama = {"BTC":2008, "ETH": 2012}

elon = {"DOGE": 6942058008}

satoshi = {"BTC": 1000000}

vitalik = {"SHIB": 410241996771871.894771826174755464}


people = [keanu, obama, elon, satoshi, vitalik]


# CONSTANTS

KEY = "REPLACE_WITH_YOUR_KEY" # Get your own nomics API key at https://p.nomics.com/cryptocurrency-bitcoin-api

URL = "https://api.nomics.com/v1/currencies/ticker?key=" + KEY

CURRENCY = "AUD"
				# Higher SLEEP_TIME means less likelihood of a call repeating previous
SLEEP_TIME = 7 			# call results, which means values are static less often, but means
               			# actual accuracy is lower as values get more disconnected from current
CRED    = '\033[91m'
CGREEN  = '\33[32m'
CYELLOW = '\033[93m'                                                        # Colour codes, constants 
CBOLD   = '\33[1m'                                                          # purely for readability
CITALIC   = '\33[3m'
CEND    = '\033[0m'


def build_params_from_all_portfolios(list_of_portfolio_dicts):
    cryptos = []
    for portfolio_dict in list_of_portfolio_dicts:
        for crypto in portfolio_dict["owned"].keys():                       # Gathers all unique crypto  
            if crypto not in cryptos:                                       # IDs to add to params for
                cryptos.append(crypto)                                      # API call
    ids = ','.join(cryptos)
    params = {"ids": ids,"convert": CURRENCY, "exchange": "coinbase"}
    return params


def build_portfolio(portfolio):
    dictionary = {"owned": portfolio,
                  "current": 0,
                  "increment": 0,                                           # Initializes a portfolio
                  "goal": 0,
                  "name": var_name_retriever(portfolio)}
    return dictionary


def build_portfolio_list(people):                                           # Builds list of portfolios 
    portfolio_list = []                                                     # (calling build_portfolio() 
    for name in people:                                                     # to populate each properly)
        portfolio_list.append(build_portfolio(name))
    return portfolio_list


def get_current_market():
    try:                                                                    # Tries to call API, sometimes 
        response = requests.get(URL, params).json()                         # the call fails in which case 
    except:                                                                 # it waits 1.1 seconds and 
        time.sleep(1.1)                                                     # recursively calls itself
        response = get_current_market()
    return response


def calculate_current_total(portfolio, market):
    total = 0                                                               # Calculates the value of a 
    for crypto in market:                                                   # portfolio using the market
        if crypto["id"] in portfolio["owned"]:                              # values and portfolio["owned"]
            owned = portfolio["owned"]
            total += float(crypto["price"]) * float(owned[crypto['id']])
    return total


def calculate_increment(portfolio):                                         # Calculates the increment required 
    return (portfolio["goal"] - portfolio["current"]) / (10 * SLEEP_TIME)   # to update 10x per second and reach 
                                                                            # goal within SLEEP_TIME


def var_name_retriever(bar):
    return (list(globals().keys()))[list(map(lambda x: id(x),               # Returns the name of a variable as a string
            list(globals().values()))).index(id(bar))]


def add_to_string(string, portfolio):
    if portfolio["increment"] > 0:
        colour = CGREEN
    elif portfolio["increment"] < 0:                                        # Concatenates portfolio to string (with 
        colour = CRED                                                       # formatting information) ready to print
    else:
        colour = CYELLOW
    string += '{}{}{}{}: ${:.2f}   {}'.format(colour, CBOLD, CITALIC, portfolio["name"], portfolio["current"], CEND)
    return string


portfolios = build_portfolio_list(people)
params = build_params_from_all_portfolios(portfolios)

print("\n\n\n\n")

# MAIN LOOP

while True:
    market = get_current_market()
    for portfolio in portfolios:
        portfolio["goal"] = calculate_current_total(portfolio, market)
        portfolio["increment"] = calculate_increment(portfolio)

    for i in range((10 * SLEEP_TIME)):
        time.sleep(0.1)
        portfolios_string = " "
        for portfolio in portfolios:
            portfolio["current"] += portfolio["increment"]
            portfolios_string = add_to_string(portfolios_string, portfolio)
        print(portfolios_string, end="\r"),

    for portfolio in portfolios:
        portfolio["current"] = portfolio["goal"]
