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
        messaggio.attach(MIMEText("""
        <div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature">
           <div dir="ltr">
              <div dir="ltr" style="color:rgb(34,34,34)">
                 <div dir="ltr">
                    <table style="border:none;border-collapse:collapse">
                       <tbody>
                          <tr style="height:97.5pt">
                             <td style="font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;vertical-align:top;padding:1pt;overflow:hidden">
                                <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt"><span style="font-size:11pt;font-family:&quot;Century Gothic&quot;,sans-serif;color:rgb(0,112,192);background-color:transparent;font-weight:700;vertical-align:baseline"><span style="border:none;display:inline-block;overflow:hidden;width:105px;height:119px"><img width="96" height="96" style="font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color:rgb(34,34,34);font-size:small;font-weight:normal" src="https://ci3.googleusercontent.com/mail-sig/AIorK4w4nSHr1kDU_WKfBOztCV-BnSeECCaFh2W5NAGXEHS_Q-6O2KcGE-Lrn5xgYb3Fdkh3zElU9hM" class="CToWUd" data-bit="iit"></span></span></p>
                             </td>
                             <td style="font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;vertical-align:top;padding:1pt;overflow:hidden">
                                <p dir="ltr" style="line-height:1.655;margin-top:0pt;margin-bottom:0pt"><span style="font-size:8.5pt;font-family:&quot;Century Gothic&quot;,sans-serif;color:rgb(68,111,179);background-color:transparent;vertical-align:baseline">Simone Vetere</span></p>
                                <p dir="ltr" style="line-height:1.655;margin-top:0pt;margin-bottom:0pt"><font color="#446fb3" face="Century Gothic, sans-serif"><span style="font-size:11.3333px">Developer</span></font></p>
                                <p dir="ltr" style="line-height:1.655;margin-top:0pt;margin-bottom:0pt"><span style="font-size:8.5pt;font-family:&quot;Century Gothic&quot;,sans-serif;color:rgb(68,111,179);background-color:transparent;vertical-align:baseline">VETERE TECH</span></p>
                                <p dir="ltr" style="line-height:1.655;margin-top:0pt;margin-bottom:0pt"><span style="font-size:8.5pt;font-family:&quot;Century Gothic&quot;,sans-serif;color:rgb(68,111,179);background-color:transparent;vertical-align:baseline">Mobile +39 392 756 0000</span></p>
                                <p dir="ltr" style="line-height:1.655;margin-top:0pt;margin-bottom:0pt"><span style="font-size:8.5pt;font-family:&quot;Century Gothic&quot;,sans-serif;color:rgb(68,111,179);background-color:transparent;vertical-align:baseline"><a href="mailto:cristian.margiaria@tesisquare.com" style="color:rgb(17,85,204)" target="_blank">simoneveterex@gmail.com</a></span></p>
                                <p dir="ltr" style="line-height:1.655;margin-top:0pt;margin-bottom:0pt"><a href="https://www.vetere.tech" style="color:rgb(17,85,204)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.vetere.tech&amp;source=gmail&amp;ust=1694180499428000&amp;usg=AOvVaw0BBIuoiwAC45vnWa4isVul"><span style="font-size:8.5pt;font-family:&quot;Century Gothic&quot;,sans-serif;color:rgb(68,111,179);background-color:transparent;vertical-align:baseline">www.vetere.tech<br></span></a></p>
                             </td>
                          </tr>
                       </tbody>
                    </table>
                 </div>
              </div>
           </div>
        </div>
        ""","html"))
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
