
import requests
url = 'http://files.cod3r.com.br/curso-js/funcionarios.json'


resp = requests.get(url=url)
data = resp.json()

