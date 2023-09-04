from flask import Flask
import smtplib
from flask import request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
    
app = Flask(__name__)
    
@app.route('/sendmail')
def sendmail():
        
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    s.login("simoneveterex", "")
    try:
        #url params
        mailto = request.args.get('mailto')
        oggetto = request.args.get('oggetto')
        testo = request.args.get('testo')


        messaggio = MIMEMultipart()
        messaggio["From"] = "simoneveterex@gmail.com"
        messaggio["To"] = mailto
        messaggio["Subject"] = oggetto
        corpo = testo
        
        messaggio.attach(MIMEText(corpo, "plain"))

        s.sendmail("no-reply@vetere.tech", mailto, messaggio.as_string())
        s.quit()
        
    except Exception as e:
        recupero = str(e)        
        try:
            if mailto != None:
                recupero = recupero + ' mailto ' + str(mailto)
            if oggetto != None:
                recupero = recupero + ' oggetto ' + str(oggetto)
            if testo != None:
                recupero = recupero + ' testo ' + str(testo)
        except:
            recupero = ''
            
        s.sendmail("simoneveterex@gmail.com", "simoneveterex@gmail.com", recupero)
        s.quit()
        
        return "ops.. c'è stato un errore"

    return 'mail inviata correttamente'



if __name__ == '__main__':
    app.run(host='0.0.0.0')
