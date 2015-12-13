from DropboxDownloader import DropboxDownloader

# Initialise the object and give it the folder to store its downloads in
d = DropboxDownloader('/Users/robin/ThesisFilesDropboxLog')

# Download all available previous versions
d.download_history_for_files("/Users/robin/Dropbox/_PhD/_FinalThesis",  # Folder containing files to download
                             "*.tex",  # 'glob' string specifying files to download
                             "/Users/robin/Dropbox/")  # Path to your Dropbox folder
