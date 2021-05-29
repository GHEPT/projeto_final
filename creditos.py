import time
from som import som

def creditos():
    credenciais = {
        'Som de varrendo':  'usuário 170084 em freesound.org',
        'Som de cozinha': 'usuário szegvari em freesound.org',
        'Som de dormindo': 'usuário 180334__sankalp em freesound.org'
    }

    for i in credenciais.items():
        print(f'{i[0]} por {i[1]}') 
        som('beep')
        time.sleep(1)

    return credenciais.items

