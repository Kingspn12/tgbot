import helpers.streamtape_u

def exec_streamtapeul(client, message):
    msg_id = message.id
    chat_id = message.chat.id
    client.send_message(chat_id = chat_id, text ="Processing...")
    print("Processing")
    try:
       client.download_media(message, file_name="video.mp4")
    except Exception as e:
        print(e)
    uploaded_url = helpers.streamtape_u.upload_video()
    client.send_message(chat_id = chat_id, text = f'Uploaded! Here is Your URL:\n{uploaded_url}', reply_to_message_id=msg_id, disable_web_page_preview = True)
