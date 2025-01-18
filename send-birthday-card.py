import smtplib
import random
import datetime
import time

def send_birthday_email():

    sender_email = "delaramdonyavi1388@gmail.com"
    receiver_email = "fatemehebrahimi.0az@gmail.com"
    password = "jxoe knoc ysmo vvra"

    name = input("Who is your target?")

    message1 = f"Dear {name} , Happy birthday!All the best for the year!...Delaram"
    message2 = f"Dear {name},Its our birthday have a great day!All my love,...Delaram"
    message3 = f"Hy {name},Happy birthday have a wonderful time today and eat a lots of cake!Lots of love,...Delaram"

    messages = [message1, message2, message3]

    random_message = random.choice(messages)
    print(random_message)


    target_birthday = datetime.datetime(datetime.datetime.now().year,2,14)


    while True :

        current_time = datetime.datetime.now()

        if current_time.date() == target_birthday.date() :

            try:
                server = smtplib.SMTP("smtp.gmail.com")
                server.starttls()
                server.login(user=sender_email, password=password)
                server.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=random_message)
                print("Weekly email sent successfully!")
            except Exception as e:
                print(f"Error: {e}")
            # finally:
            #     server.quit()
send_birthday_email()




