# Dropbox-based Word Count

Code for doing downloading all previous versions of a file from Dropbox, and
then doing LaTeX word counts on the files. This can easily be used without the
word count step, if you just have some files whose entire history you want to get.

`DropboxDownloader.py` contains the code to do the actual downloading from Dropbox
`example.py` contains an example of how to run the above code
`process.py` contains some very rough and poorly written code for running `texcount` and doing analysis
