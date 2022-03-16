import requests
try:
    response = requests.get('http://www.pudim.com.br/')
except(ValueError, TypeError):
    print('O site Pudim não está acessivel no momento')
except KeyboardInterrupt:
    print('O site Pudim não está acessivel no momento')
except Exception as erro:
    print(f'O site Pudim não está acessivel no momento')
else:
    print('Consegui acessar o site Pudim com secesso!!')