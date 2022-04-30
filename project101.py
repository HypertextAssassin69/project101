import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BGv4eMEDAMjIgIvNhWEKYw3UEONPong-7jokizcOwpinqkjFoLf313Xsvo6Vb5VvnY12HAM2fJQBiRUFEzReCcFUqynDM9JJlTer9KBFG_rCOY7B7c-ayeWvzVt7yIhwksMS-5mHzmBb'
    transferData = TransferData(access_token)

    file_from = input("enter the full path of the file with the file that you u want to backup with forward slash(/): ")
    file_to = input("enter the file path in which u want to backup ur files in dropbox with forward slash(/): ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


main()