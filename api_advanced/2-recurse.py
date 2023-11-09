#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """ returns a list with titles of all hot articles in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if response.status_code == 200:
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for child in children:
                    hot_list.append(child.get('data').get('title'))
                    if len(hot_list) >= 2:  # Limit the number of titles to 2
                        return hot_list
                after = data.get('after')
                if after is not None:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
        else:
            return hot_list
    else:
        return None
