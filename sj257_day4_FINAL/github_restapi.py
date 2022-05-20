'''Goal:  Practice generic API skills

Many REST APIs also have authentication (username and password)
and may also have session tokens.  We COULD do this with urllib
but it is much easier with the Requests package.

    https://docs.python-requests.org/en/latest/

To install from the command line:

    $ python3.10 -m pip install requests

'''

from urllib.request import urlopen
import json

def show_github_account(username):
    "Display a Github user's id, name, and location"
    # GitHub REST API is documented at:
    # https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api
    url = f'https://api.github.com/users/{username}'
    with urlopen(url) as f:
        info = json.load(f)
    print(f"User {info['id']} is {info['name']} in {info['location']}")

if __name__ == '__main__':
    
    show_github_account('raymondh')
    show_github_account('hugs')
    show_github_account('vstinner')
