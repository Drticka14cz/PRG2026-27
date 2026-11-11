from bs4 import BeautifulSoup
import requests

def main():

    url = "https://www.trebesin.cz"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    gym = soup.select_one("#favimagehover-title4")
    
    print(gym.text)

    headings = soup.select("h4")
    # print(headings)
    for i in headings:
        print(i.text.strip())


if __name__ == "__main__":
    main()