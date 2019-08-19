import ftplib

ftp = ftplib.FTP()

def file_search():
    ftp.connect('10.16.*.*', 21)
    ftp.login("user", "passwd")
    return ftp.nlst()


def upload_file(file_name):
    f = open(file_name, "rb")
    print("STOR "+file_name)
    ftp.storbinary("STOR %s" % file_name, f, 1024)


file_search()