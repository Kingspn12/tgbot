import helpers.pingtest

def exec_ping(client, message):
    chat_id = message.chat.id
    ping = helpers.pingtest.test_ping()
    if ping is not int:
        client.send_message(chat_id = chat_id, text = "Speedtest Server Error")
    client.send_message(chat_id = chat_id, text = f"Pong : `{ping} ms`")
