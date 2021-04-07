import requests
import json
import pandas as pd

headers = {
    'Ocp-Apim-Subscription-Key': '0a5782c351ba49909e7de6fe63d06960',
}

scraped_company_data, temp = [], []
list_of_companies = ['Microsoft', 'Intel', 'Cisco']

for company in list_of_companies:
    list_of_queries = [f'disabled employee news at {company}', f'employee accessibility news stories {company}',
                       f'{company} name erg disability news', f'disabled employee news blogs {company}',
                       f'accessibility statement news {company}', f'accommodation statement news {company}',
                       f'interview accommodations news {company}']
    for query in list_of_queries:
        params = (
            ('q', query),
            ('count', '50'),
        )
        response = requests.get('https://api.bing.microsoft.com/v7.0/search', headers=headers, params=params)
        loaded_dict = (json.loads(response.content.decode("utf-8")))

        for key, value in loaded_dict.items():
            if key == 'webPages':
                for k, v in value.items():
                    if k == 'value':
                        list_urls = v

        for i, element in enumerate(list_urls):
            scraped_company_data.append([company, query, element['url'], element['name'], element['snippet']])

scraped_company_df = pd.DataFrame(scraped_company_data, columns=['Company Name', 'Query', 'URL', 'Name of Web Page',
                                                                 'Web Page Snippet'])
scraped_company_df.to_csv('output_second_python_search.csv')