# Automatic Email Sender

**Introduction**

This Python script allows you to send an email using SMTP (Simple Mail Transfer Protocol). The script uses Gmail's SMTP server to send emails, requiring an App Password for authentication.

**How SMTP Works**

SMTP (Simple Mail Transfer Protocol) is a protocol used for sending emails over the internet. Here's how it works:

Connect to the SMTP Server: The script connects to smtp.gmail.com using port 587 (TLS) for secure communication.
Start TLS Encryption: The connection is encrypted to ensure security.
Authenticate the Sender: The sender logs in using their email address and an App Password (not the normal Gmail password).
Send the Email: The email is sent from the sender's Gmail account to the recipient.
Close the Connection: The SMTP session is terminated after sending the email.

**Prerequisites**

1.Python 3 installed
2.A Gmail account
3.An App Password (mandatory)

**How to Generate an App Password for Gmail**

Google does not allow normal passwords for SMTP. You must generate an App Password.
Enable 2-Step Verification (if not already enabled):
Go to Google Account Security
Scroll down to "How you sign in to Google"
Click on "2-Step Verification" and enable it

Generate an App Password:
Go to Google App Passwords
Sign in if prompted
Under "Select App", choose "Mail"
Under "Select Device", choose "Windows Computer"
Click "Generate"

Copy the 16-character App Password (e.g., abcd efgh ijkl mnop)

Use this password in your script (without spaces)

**ScreenShots**
![Screenshot 2025-03-02 222052](https://github.com/user-attachments/assets/3e63c13b-7fee-41a2-8943-1e177d0ad5d1)
![Screenshot 2025-03-02 222214](https://github.com/user-attachments/assets/afc1be60-af1c-4a8f-b9b7-f67c295d5e38)

**Troubleshooting**

1. SMTP Authentication Error?

Ensure you're using an App Password, not your regular Gmail password.

Make sure 2-Step Verification is enabled.

2. Firewall/Antivirus Blocking SMTP?

Temporarily disable your firewall/antivirus and try again.

3. Email Not Received?

Check your Spam folder.

Ensure the recipient's email is correct.

**Conclusion**

This script allows you to send automated emails using Python and SMTP. By following the correct authentication steps (using an App Password), you can securely send emails from your Gmail account.

Enjoy coding! 🚀

