
import time
import sinchsms
from time import sleep
from sinchsms import SinchSMS

def sendSMS():
    # Receiptent mobile number
    number = '9550534128'

    # User details of Sinch
    # Beta dashboard: https://dashboard.sinch.com/dashboard/
    app_key = '01FZC183W6B422VD79APYJWJ8S'
    app_secret = 'd32912c4e25f43269c1807624abf7a1a'

    # Message to send
    message = 'Hello!!'

    # Connection String
    client = SinchSMS(app_key, app_secret)
    print(f'Sending{message} to {number}')  # Process notification

    
    response = client.send_message(number, message)
    message_id = response('messageId')
    response = client.check_status(message_id)

    while response['status'] != 'Successful':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)

    print(response['status'])


if __name__ == '__main__':
    sendSMS()