from bs4 import BeautifulSoup
import requests
from constants import _URL, _AGENT

def get_url(url):
    cont=0
    # Get the URL from the user, but we don't know how many pages there are, so we'll just keep asking until we get a valid URL
    while True:
        url = url+str(cont)
        if requests.get(url, headers=_AGENT).status_code == 200:
            return url


def main():
    pass

if __name__=="__main__":
    
    pass 