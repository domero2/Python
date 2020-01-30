import requests
import pprint
from lxml import html






r = requests.get('https://api.github.com')
pprint.pprint(r.json()['authorizations_url'][0])
response = requests.get('https://api.github.com').json()
#returnn5 = response.keys()[0]
returnn=next(iter(response.values()))
returnn2=next(iter(response.keys()))
print(response)
print(returnn)
print(returnn2)

