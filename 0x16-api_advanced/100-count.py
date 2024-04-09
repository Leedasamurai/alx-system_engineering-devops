#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): A parameter for pagination (default is None).
        count_dict (dict): A dictionary to store the count of each keyword (default is None).

    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for word in word_list:
                    if title.count(word.lower()) > 0:
                        if word.lower() in count_dict:
                            count_dict[word.lower()] += title.count(word.lower())
                        else:
                            count_dict[word.lower()] = title.count(word.lower())
            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print("{}: {}".format(word, count))
    else:
        print(None)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
