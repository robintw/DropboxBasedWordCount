from download import DropboxDownloader

d = DropboxDownloader('C:\Test')
d.download_history_for_files("C:\Dropbox\Dropbox\_PhD\_FinalThesis", "*.tex", "C:\Dropbox\Dropbox")
