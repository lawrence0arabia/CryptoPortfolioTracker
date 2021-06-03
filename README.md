# CryptoPortfolioTracker


### Track multiple cryptocurrency portfolios in real time.

Utilising the 🟪[Nomics API](https://nomics.com/docs/#tag/Currencies) to get crypto prices.

# FEATURES

## 😎 Smooth Value Updates

Queues 1 crypto price at a time and gradually increments every 0.1 seconds to "smoothly" update portfolio values, since nomics api has 1 second rate limit, and the actual data their api returns is only updated every ~7 seconds. Because of this, the `SLEEP_TIME` constant interval is set to 7, but you can decrease that if you would like more up-to-date valuation, or increase it to reduce the likelihood of the nomics api returning the same values (which causes the "smooth" updating to pause until nomics returns new data).

## 🧑‍🤝‍🧑🧑‍🤝‍🧑 Multiple Portfolio Support

Add as many portfolios as you want 🤙

<img width="1004" alt="multiple" src="https://user-images.githubusercontent.com/67545734/120465594-7d2b9c00-c3e1-11eb-96f9-4fbab2bd30db.png">

Some example portfolios are already present in the code: 

<img width="550" alt="portfolio_examples" src="https://user-images.githubusercontent.com/67545734/120466153-1490ef00-c3e2-11eb-9688-e6d8b3fccdca.png">

#### Adding a portolio is as easy as pi:

1. Create a new dictionary where the keys are crypto tags, and the values are the amount of that crypto the portfolio owns. 

2. Add the new dictionary to the `people` list.

The script will aggregate unique cryptocurrency tags to generate params for the api call so the api will only need to be called once for every loop 😎

## 🟢 Green For Gains, 🔴 Red For Rethink Your Financial Decisions

Crypto going up but you never learnt how to count? 
Not a problem! The script will automatically format each portfolio with colours depending on their current performance.

🟢 The latest API call returned bigger numbers than the previous API call. You're in the money 🤑 At least for now 🤡

🟡 The latest API call returned the same numbers. Darn 😠 If you want this to happen less often you could try raising the `TIME_SLEEP` constant.

🔴 Aw, shucks! You're bleeding money 😞 You should've just put your money under your bed like your grandma told you 👵

# Running Locally

- This script was built with `Python3.9` but I'm pretty sure it'd still run if you have any version of Python3. No promises though.

- You'll have to replace the `KEY` constant with your own key, which you can get from 🟪[Nomics](https://p.nomics.com/cryptocurrency-bitcoin-api).

- You should also probably replace the example portfolios, unless you want to imagine how much crypto Keanu Reeves has, or track the exact value of the 🐶 SHIB Vitalik cast into a volcano (4,635,734,563.52 dollarydoos 💵🦘 at the time of the screenshot above taken on June 1st).

- Oh yeah, and you should probably change the CURRENCY constant from `"AUD"` to `"USD"` or something if you're not from Australia 🇦🇺, but I'm kinda assuming anyone reading this is from here since I'm not applying for jobs anywhere else 🤷‍♀️
