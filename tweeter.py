#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Randomly display archived tweets for recycling. This project is
deliberately stripped down for demonstration purposes.
"""

import os
import re
import random
import requests

# The maximum tweet length to check against (Twitter max is 280)
MAX_CHARS = 260


def main():
    """
    Execution starts here.
    """

    # Choose a random file from the text/ directory
    files = os.listdir("text")
    filename = f"text/{random.choice(files)}"

    # Open the file and read in all the text
    with open(filename, "r") as handle:
        text = handle.read()

    # Perform a quick length check
    chars = len(text)
    if chars >= MAX_CHARS:
        print(f"{filename}: Message to long -> {chars} < {MAX_CHARS}")
        print(80 * "-")

    # Perform a quick URL check to ensure link is valid (if a URL exists)
    url_search = re.search(r"(?P<url>https?://[^\s]+)", text)
    if url_search:
        url = url_search.group("url")
        resp = requests.head(url, allow_redirects=True)

        # Can't just test for resp.ok, we want unfollowed redirects to fail
        if resp.status_code != 200:
            print(f"{url}: HEAD failed -> {resp.status_code} / {resp.reason}")
            print(80 * "-")

    # Print the tweet text for copy/paste
    print(text)


if __name__ == "__main__":
    main()
