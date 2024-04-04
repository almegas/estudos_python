import smtplib

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("almegas08@gmail.com", "ihok jopz irtz qnre")
    server.sendmail(
     "almegas08@gmail.com",
     "almegas08@gmail.com",
     "teste de msg")
except Exception as e:
    print(f"Erro ao enviar email: {e}")
finally:
    server.quit()





