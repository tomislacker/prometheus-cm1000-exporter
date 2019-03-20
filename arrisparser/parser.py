"""
arrisparser.parser
==================
Parses an HTML document from an Arris modem
"""
from __future__ import print_function
import json
import re

from bs4 import BeautifulSoup


NAME_CLEANER = re.compile(r'[^a-zA-Z0-9-_]+')
WHITESPACE = re.compile(r'\s+')


def clean_name(name):
    return NAME_CLEANER.sub('', name)


def clean_value(value):
    value = WHITESPACE.split(value, 1)[0]

    try:
        value = float(value)
    except ValueError:
        pass
    return value


def from_html_string(html_doc):
    soup = BeautifulSoup(html_doc, 'html5lib')
    data = {}
    for tbl in soup.find_all('table', {'class': 'simpleTable'}):
        table_name = clean_name(tbl.find('th').getText())
        data[table_name] = []
        fields = []

        for tr in tbl.find_all('tr'):
            if len(tr.find_all('td')) <= 1:
                # Ignore this as it's a table header
                continue

            if not fields:
                # We haven't determined the fields yet so use this first
                # row to determine those
                fields = [
                    clean_name(td.getText())
                    for td in tr.find_all('td')
                ]

            else:
                # This is a part of the "body"
                row = {}
                for tdidx, td in enumerate(tr.find_all('td')):
                    try:
                        field_name = fields[tdidx]
                    except IndexError:
                        field_name = f'idx-{tdidx}'

                    row.update({
                        field_name: clean_value(td.getText().strip()),
                    })
                data[table_name].append(row)

    print('<data>')
    print(json.dumps(data, indent=4, sort_keys=True))
    print('</data>')

    return data


if __name__ == '__main__':
    with open('tests/data/status.html', 'r') as infile:
        html_doc = infile.read()

    from_html_string(html_doc)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
