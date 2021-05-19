from slack_sdk import WebClient
from time import sleep
if __name__ == "__main__":
    slack_token="xoxp-1572449625687-1599853209169-1611081155408-6004cd50f7188bc212c670c1592a14bd"
    client=WebClient(token=slack_token)
    response=client.files_upload(channel="C01HFBEG5RA",file="abc.txt",text="Test upload")
    print(response)
    client=WebClient(token="xoxb-1572449625687-1587239145218-dGRWEztllofSYoGUTVyDrY4M")
    response=client.files_remote_add(
        external_id="test",
        external_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.pixelstalk.net%2Fwp-content%2Fuploads%2F2016%2F06%2FDesktop-Wallpaper-HD-Free-Download.jpg&f=1&nofb=1",
        title="test",
        preview="./preview.jpg"
    )
    print(response)
