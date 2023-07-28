import requests
import uuid

key = "9dc657830ee34a3396040554c8bdf447"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "centralindia"


def translate(language_code, word):
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': language_code
    }
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': word
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    translated_word = response[0]['translations'][0]['text']

    return translated_word


if __name__ == "__main__":
    from supported_languages import get_language_codes
    from word import get_random_word

    language_code = get_language_codes()["Malayalam"]
    word = get_random_word()
    translation = translate(language_code[1], word)
    print(word, translation)
