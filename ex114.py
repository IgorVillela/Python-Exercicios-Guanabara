import requests


def verifica_status_do_site(url):
    try:
        resposta = requests.get(url)
        # Verifica se a resposta foi bem-sucedida (código de status 2xx)
        if resposta.status_code // 100 == 2:
            print(f'\033[1;32mO site {url} está acessível. Código de status: {resposta.status_code}\033[m')
        else:
            print(f'\033[1;31mO site {url} retornou um código de status não esperado: {resposta.status_code}\033[m')
    except requests.ConnectionError:
        print(f'\033[1;31mNão foi possível conectar-se ao site {url}. Verifique sua conexão com a Internet.\033[m')


# Principal
url_do_site = 'https://www.google.com'
verifica_status_do_site(url_do_site)
