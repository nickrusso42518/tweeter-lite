[![Build Status](
https://travis-ci.com/nickrusso42518/tweeter-lite.svg?branch=master)](
https://travis-ci.com/nickrusso42518/tweeter-lite)

# Lightweight Tweet Validator
This project can be used to verify Twitter messages (tweets) against
two constraints:
  1. **Length**: tweets can be only so long
  2. **Valid URL**: If you embed a URL use Python `requests` to ensure it works

Install the required packages with `pip install -r requirements.txt`.

Then, run the script with `python tl.py`.

If the length is too long, you'll see a message like this:
```
bad/long.txt: Message to long -> 283 < 260
-------------------------------------------------------
```

If the URL does not return status 200 (OK), you'll see a message like this:
```
http://njrusmc.net/bad: HEAD failed -> 404 / Not Found
-------------------------------------------------------
```

Regardless, the text of the tweet is printed out last, allowing for easy
copy/paste into Twitter. The absence of any error messages is an indication
that the tweet has passed all tests.
