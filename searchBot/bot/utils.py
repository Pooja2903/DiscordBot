import urllib
import requests
import traceback

from searchBot.bot.models import SaveSearch


def search_api_call(keyword):
    """
    Google search the keyword using api and return top5 results
    :param keyword:
    :return:
    """
    headers = {
        'x-rapidapi-key': "f09eeb5dabmshdb9b8b738400cfdp1a2926jsn129c82b26be5",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }

    query = {
        "q": keyword,
        "num": 50
    }
    url = "https://google-search3.p.rapidapi.com/api/v1/search/" +  urllib.parse.urlencode(query)
    top_links = []
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.text)
        search_results = response.json()
        results = search_results.get('results', [])
        if results:
            list_len = len(results) if len(results) < 5 else 5
            for itr in range(list_len):
                top_links.append(results[itr].get('link'))
    except Exception as exc:
        print("Exception: %s, trace: %s", exc, traceback.format_exc().replace('\n', ' | '))

    return top_links


def save_keyword(message_author, keyword):
    """
    Save keyword into database to be used for searching
    :param message_content:
    :param keyword:
    :return:
    """
    SaveSearch.objects.create(author=message_author, keyword=keyword)


def get_db_search_results(keyword):
    """
    Search keyword in db and return results which contain the keyword
    :param keyword:
    :return:
    """
    queryset = SaveSearch.objects.filter(keyword__contains=keyword)

