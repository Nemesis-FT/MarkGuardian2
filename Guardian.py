 import time
  import smtplib
  import os
 +import sys
  payload = {
 +    'ob_user': sys.argv[1],
 +    'ob_password': sys.argv[2],
  }
  #Codice scritto da Balugani Lorenzo con il contributo di Stefano Pigozzi. Questo software èompatibile con il sistema di LOAR.
  with requests.session() as c:
      first = 1
      print("Servizio MarkGuardian 2 in avvio. LBcorporation, LBservices.")
      print("Del codice molto importante e'stato scritto anche da Stefano Pigozzi!")
 -    pw = input('Immetti la password di info.lbcorporation@gmail: ')
 -    os.system('clear') #va solo su sistemi unix!
      print("MarkGuardian sta ora cercando delle modifiche sulla pagina del registro...")
      print("--------------------------------------------------------------------------")
      while True:
              print("!!! FILE MODIFICATO !!!")
              server = smtplib.SMTP('smtp.gmail.com', 587)
              server.starttls()
 -            server.login("info.lbcorporation", pw)
 +            server.login(sys.argv[3], sys.argv[4])
              msg = "Ciao! Sembra che ci sia un nuovo voto sul sito!"
 +            server.sendmail(sys.argv[5], sys.argv[6], msg)
              server.quit()
          time.sleep(1000)
      print("I messed up.")
