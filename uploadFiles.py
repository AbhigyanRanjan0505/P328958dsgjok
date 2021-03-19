import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as file_:
                    dbx.files_upload(file_.read(), dropbox_path,
                                     mode=WriteMode('overwrite'))


token = input("Enter your dropbox token: ")
transferData = TransferData(token)

file_from = str(input("Enter the file/folder path to transfer: "))
to = input("Enter the path from dropbox to location you want to store: ")
transferData.upload(file_from, to)

print("File has been moved to dropbox successfully!!!")
