from slack_sdk import WebClient
if __name__ == "__main__":
    slack_token="xoxp-1572449625687-1599853209169-1611081155408-6004cd50f7188bc212c670c1592a14bd"
    client=WebClient(token=slack_token)
    try:
        response = client.chat_postMessage(channel="C01HFBEG5RA",
        text="Hello boy")
        #response1=client.chat_postEphemeral(channel="C01HFBEG5RA",
        #text="Hello boy hdb",user="D01H2EKPWAJ")
        print(response)
    except Exception as e:
        print(str(e))    