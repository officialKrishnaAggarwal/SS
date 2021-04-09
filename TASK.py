import dropbox
import time

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token='da_JMVBquzwAAAAAAAAAAVT4RiVl0C8df5ot9IJnBOl9DNu4nUyOCZjROSv-i94n'
    
    file="D:/test.txt"
    fileread=open(file, 'r')
    filewrite=open(file, 'w')
    text=input("Enter your message: ")
    filewrite.write(text)


    time.sleep(5)
    transferData=TransferData(access_token)
    file_from="D:/test.txt"
    file_to="/Test/test.txt"
    transferData.upload_file(file_from, file_to)
    print("Done")

main()
