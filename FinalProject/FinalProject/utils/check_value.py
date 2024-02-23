def check_value_of_message(message_text):
    try:
        x = int(message_text) / 23

        if int(message_text) <= 50:
            return True

        return False
    except Exception as error:
        print(error)
        return False

