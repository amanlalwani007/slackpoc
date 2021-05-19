from slack_sdk import WebClient
from time import sleep
if __name__ == "__main__":
    slack_token="xoxp-1572449625687-1599853209169-1611081155408-6004cd50f7188bc212c670c1592a14bd"
    client=WebClient(token=slack_token)
    try:
        response=client.chat_postMessage(channel="C01HFBEG5RA",
        text="Hello boy")
        thread_timestamp=response['ts']
        print(response)
        sleep(10)
        response1=client.chat_update(channel="C01HFBEG5RA",text="Hi Aman",ts=thread_timestamp)
        print(response1)
    except Exception as e:
        print(str(e))    