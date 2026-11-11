from bs4 import BeautifulSoup
import requests

def main():

    url = "https://www.moodle-trebesin.cz/"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    gym = soup.select("div>h5")
    for i in gym:
        print(i.text.strip())
    
   


if __name__ == "__main__":
    main()