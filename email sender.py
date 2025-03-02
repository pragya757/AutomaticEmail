import smtplib

def automatic_email():
    user = input("Enter Receiver's Name >>: ")
    email = input("Enter Receiver's Email >>: ")
    message = f"Subject: Test Mail!!\n\nDear {user}, Hello! This is a test email from Python. "

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("betapro757@gmail.com", "jpkc ayex dwru jrgi")  
        s.sendmail("betapro757@gmail.com", email, message)
        s.quit()
        print("Email Sent Successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Error: SMTP Authentication failed. Check your credentials or enable App Password.")
    except Exception as e:
        print(f"An error occurred: {e}")

automatic_email()
