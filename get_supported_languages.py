from bs4 import BeautifulSoup
import requests

url = "https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support"


def get_language_codes():
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    translation_table = soup.find("table")
    table_body = translation_table.find("tbody")

    language_dict = {}
    if table_body:
        rows = table_body.find_all("tr")

        for row in rows:
            cells = row.find_all("td")[:2]

            language_dict[cells[0].text.strip()] = cells[1].text.strip()

        return language_dict


if __name__ == "__main__":
    print(get_language_codes())
