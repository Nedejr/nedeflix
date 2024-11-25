import requests

class Auth:
    
    def __init__(self):
        self.__base_url = 'https://nedejr.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        payload = {
            'username' : username,
            'password' : password
        }
        response = requests.post(url=self.__auth_url, data=payload)


        if response.status_code == 200:
            return response.json()
        return {'error': f'Erro ao autenticar. Status Code: {response.status_code}'}
