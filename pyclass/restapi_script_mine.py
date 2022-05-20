import json
from urllib.request import urlopen

#url = 'https://api.github.com/users/raymondh'
def show_github_account(username):
    url = 'https://api.github.com/users/raymondh'
    with urlopen(url) as f:
        #page = f.read().decode()
        #print(page)
        info = json.load(f)
        print(f"User {info['id']} is {info['name']} in {info['location']}")


if __name__ == '__main__':
    show_github_account('raymondh')
