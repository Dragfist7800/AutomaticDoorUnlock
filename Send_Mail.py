import yagmail
import os


def sendMail(img):
    #files = img
    #filename = files
    sub = "Unknown person requesting access"
    # mail information
    yag = yagmail.SMTP("gatekeeperwastaken@gmail.com", "!@#$%^&*()1234567890Gatekeeper")

    # sent the mail
    yag.send(
        subject=sub,
        to="tkksctwo@gmail.com",  # email subject
        contents="This person is requesting access to R & D cell",  # email body
        #attachments=filename  # file attached
    )
    print("Email Sent!")
sendMail("asdas")
