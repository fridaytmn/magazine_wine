from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime
import pandas as pd
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_drinks():
    result_wines = defaultdict(list)
    excel_data_df = pd.read_excel('wine3.xlsx',
                                  na_values=None,
                                  keep_default_na=False
                                  )
    wines = excel_data_df.to_dict(orient='records')
    for wine in wines:
        result_wines[wine['Категория']].append(wine)
    category_drinks = sorted(list(result_wines.keys()))
    return [category_drinks, result_wines]


def correct_name_year(now_age: int) -> str:
    now_age = now_age % 100
    if now_age < 21 and now_age > 4:
        return 'лет'  
    elif now_age % 10 == 1:
        return 'год'
    elif now_age % 10 > 1 and now_age % 10 < 5:
        return 'года'
    return 'лет'


actual_year = datetime.now().year
now_age = actual_year - 1920

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
    )

template = env.get_template('template.html')

rendered_page = template.render(
    now_age=now_age,
    name_year=correct_name_year(now_age),
    wine=get_drinks()[1],
    category_drinks=get_drinks()[0]
    )

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
