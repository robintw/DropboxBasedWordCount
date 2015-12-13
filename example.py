from download import DropboxDownloader

d = DropboxDownloader('/Users/robin/ThesisFilesDropboxLog')
d.download_history_for_files("/Users/robin/Dropbox/_PhD/_FinalThesis", "*.tex", "/Users/robin/Dropbox/")
