# Path to file to load urls.
LOAD_PATH = 'urls.json'

# You can load urls partially.
# Example: `START_FROM = 0, END_AT = 20` will perform [0, 20).
START_FROM = None
END_AT = None

# Path to save your results.
SAVE_PATH = 'results.json'

# Path to save your failed attempts.
FAILED_PATH = 'failed.json'

# You can save your results indented for a clearer view. (It could reduce the performance.)
PRETTIFY_JSON = False

# You can sort your results by it's keys.
SORT_KEYS = False

# Define how many requests you'll send at the same time.
TRESHOLD = 100

# Define how many seconds you'll wait between bulk requests.
SLEEP_TIME = 1

# HTTP Request headers.
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7'
}
