import helpers.streamtape_d
import os


def exec_streamtapedl(client, message):
 
    text = message.text[10:]
    print(text)
    msg_id = message.message_id
    chat_id = message.chat.id
    if text == "":
        client.send_message(chat_id=chat_id, text="Enter a Streamtape Link")
    else:
        
        
        result = helpers.streamtape_d.streamtape_dl(text)
        if result is True:
            print("Uploading...")
            client.send_message(chat_id = chat_id, text = "Uploading...", reply_to_message_id = msg_id)
            client.send_video(chat_id=chat_id, video = open("video.mp4","rb"))
            print("Sent")
            directory = os.getcwd()
            os.remove(directory + "/video.mp4")
            print("video is cleaned")
        else:
           client.send_message(chat_id = chat_id, text = "Result not found", reply_to_message_id = msg_id) 
        
