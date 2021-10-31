import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
    def main():
        access_token='sl.A7ex6w66VAKtO5ysdPi82ha_PyUSsIdSj37qx7hGDckYpEHhTk9iCWH-jsyFw_4cAvsoWhEmAIro__PjK65QrMDHCQRkqjIS7BfoOT6qxcBZtLVZy2MoB6Ubea8HP6RKxGRp_fc'
        transferData=TransferData(access_token)
        file_from = input("Enter the file path to transfer : -")
        file_to = input("enter the full path to upload to dropbox:- ")
    transferData.upload_file(file_from, file_to)
         print("file has been moved !!!") 
          
    main()
