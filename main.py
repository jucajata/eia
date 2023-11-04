import requests
import os
from dotenv import load_dotenv

load_dotenv()

EIA_API_KEY = os.getenv('EIA_API_KEY')
API_route = f'v2/electricity/electric-power-operational-data/data'
API_route = f'v2/electricity/electric-power-operational-data/facet/sectorid'
#url_get = f'https://api.eia.gov/{API_route}?api_key={EIA_API_KEY}&data[]=generation&facets[sectorid][]=98&facets[location][]=AZ&facets[fueltypeid][]=OTH&frequency=annual'
url_get = f'https://api.eia.gov/{API_route}?api_key={EIA_API_KEY}'
response = requests.get(url=url_get)
print(response.text)