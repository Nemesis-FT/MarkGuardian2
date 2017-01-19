import requests
import time
import smtplib
import os
import sys
payload = {
    'ob_user': sys.argv[1],
    'ob_password': sys.argv[2],
}
#Codice scritto da Balugani Lorenzo con il contributo di Stefano Pigozzi. Questo software èompatibile con il sistema di LOAR.
with requests.session() as c:
    actual = 0
    prev = 0
    first = 1
    print("Servizio MarkGuardian 2 in avvio. LBcorporation, LBservices.")
    print("Del codice molto importante e'stato scritto anche da Stefano Pigozzi!")
    print("MarkGuardian sta ora cercando delle modifiche sulla pagina del registro...")
    print("--------------------------------------------------------------------------")
    while True:
        c.post('http://www.fermi.mo.it/~loar/AssenzeVotiStudenti/elabora_PasswordStudenti.php', data=payload)
        response = c.post('http://www.fermi.mo.it/~loar/AssenzeVotiStudenti/VotiStudente1Q.php')
        actual = len(response.content)
        if actual == prev or first == 1:
            print("Pagina non modificata")
            prev = actual
            first = 0
        elif actual != prev:
            prev = actual
            print(response.content)
            print("!!! FILE MODIFICATO !!!")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sys.argv[3], sys.argv[4])
            msg = "Ciao! Sembra che ci sia un nuovo voto sul sito!"
            server.sendmail(sys.argv[5], sys.argv[6], msg)
            #server.sendmail("info.lbcorporation@gmail.com", "riccardoruozi@icloud.com", msg)
            server.quit()
        time.sleep(1000)
print("I messed up.")
