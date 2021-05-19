from slack_sdk import WebClient
import time
if __name__ == "__main__":
    slack_token="xoxp-1572449625687-1599853209169-1611081155408-6004cd50f7188bc212c670c1592a14bd"
    client=WebClient(token=slack_token)
    try:
        response=client.chat_postMessage(channel="C01HFBEG5RA",
        text="Hello boy")
        print(response)
        times=response['ts']
        time.sleep(10)
        response1=client.reactions_add(channel="C01HFBEG5RA"
        ,name="thumbsup"
        ,timestamp=times)
        time.sleep(5)
        response2=client.reactions_remove(channel="C01HFBEG5RA"
        ,name="thumbsup"
        ,timestamp=times)
        print(response2)

    except Exception as e:
        print(str(e))    