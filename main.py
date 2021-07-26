import urllib.request
from bs4 import BeautifulSoup


def main(state):
    url = "https://coronaclusters.in/"+state
    response = urllib.request.urlopen(url)

    soup = BeautifulSoup(response, "html.parser")
    value = soup.findAll('h5', {'class': 'card-title text-md text-md-lg'})
    return value[0].text, value[1].text, value[2].text, value[3].text

