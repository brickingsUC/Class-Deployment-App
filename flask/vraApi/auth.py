import  requests
#request to vRA to get auth token. This is needed for every api call and is set as a secure cookie in app.py
def api_token(username, password):
    headers = {
        'Accept': 'application/json',            
        'Content-Type': 'application/json',
    }
    data = '{"username":"' + username + '","password":"' + password + '","tenant":"vsphere.local"}'
    url = 'https://sandbox02.cech.uc.edu/identity/api/tokens'
    response = requests.post(url=url, headers=headers, data=data, verify='certs/sandbox02-cech-uc-edu-chain.pem').json()
    auth = 'Bearer ' + response['id']
    headers.update({'Authorization': auth})

    return headers

#request to check validity of token. Token needs to be valid to check so if this returns anything other than a 204, redirect to login.
def api_token_valid(request):
    token = request.cookies['Authorization']
    
    headers = {
        'Accept': 'application/json',            
        'Content-Type': 'application/json',
        'Authorization': token,
    }

    
    token = token[7:]
    url = 'https://sandbox02.cech.uc.edu/identity/api/tokens/' + token
    response = requests.head(url=url, headers=headers, verify='certs/sandbox02-cech-uc-edu-chain.pem')
    return response.status_code