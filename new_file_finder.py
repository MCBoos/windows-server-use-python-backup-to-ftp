import os
import upload_file_to_ftp

def main(dir_name):
    list = os.listdir(dir_name)
    for i in range(0, len(list)):
        path = os.path.join(dir_name, list[i])
        if os.path.isfile(path):
            # for path in upload_file_to_ftp.file_search():
                if str(path)[2:] in str(upload_file_to_ftp.file_search()):
                    print("Ftp Have %s" % path[2:])
                else:
                    print(upload_file_to_ftp.file_search())
                    print("Not Have %s" % path[2:])
                    upload_file_to_ftp.upload_file(path)


if __name__ == '__main__':
    main()
