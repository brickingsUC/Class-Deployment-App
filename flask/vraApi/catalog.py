import requests

#Request to list all catalog items user has access to.
def catalog_items(cookie):
    headers = {
        'Accept': 'application/json',            
        'Content-Type': 'application/json',
        'Authorization': cookie,
    }
    url = 'https://sandbox02.cech.uc.edu/catalog-service/api/consumer/entitledCatalogItemViews?limit=500'

    response = requests.get(url=url, headers=headers, verify='certs/sandbox02-cech-uc-edu-chain.pem').json()

    return response