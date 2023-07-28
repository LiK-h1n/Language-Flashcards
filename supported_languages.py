from bs4 import BeautifulSoup
import requests

url_1 = "https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts"
url_2 = "https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support"


def get_language_codes():
    language_dict = {}

    response = requests.get(url_1)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    speech_service_table = soup.find_all("table")[1]
    table_body_1 = speech_service_table.find("tbody")

    if table_body_1:
        rows = table_body_1.find_all("tr")

        for row in rows:
            cells = [cell for i, cell in enumerate(row.find_all("td")) if not i == 0]
            if cells[0].text.strip().split()[0] not in language_dict:
                language_dict[cells[0].text.strip().split()[0]] = [cells[1].text.strip().split()[0][:-1]
                                                                   if cells[1].text.strip().split()[0][-1].isdigit()
                                                                   else cells[1].text.strip().split()[0]]
            else:
                continue

    response = requests.get(url_2)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    translation_table = soup.find("table")
    table_body_2 = translation_table.find("tbody")

    if table_body_2:
        rows = table_body_2.find_all("tr")

        for row in rows:
            cells = row.find_all("td")[:2]

            if cells[0].text.strip().split()[0] in language_dict:
                language_dict[cells[0].text.strip().split()[0]].append(cells[1].text.strip())

    keys_to_delete = [key for key, value in language_dict.items() if isinstance(value, list) and len(value) == 1]

    for key in keys_to_delete:
        del language_dict[key]

    del language_dict["English"]

    return language_dict


if __name__ == "__main__":
    print(get_language_codes())
