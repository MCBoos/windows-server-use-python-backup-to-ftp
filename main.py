import upload_file_to_ftp
import new_file_finder
import file_zip
# import socket

# 配置信息
file_dir = './'  # 设置数据库文件所在目录

# 主函数


def main():
    new_file_finder.main(file_dir)


# !!!!!!!!!!!!RUN_BACKUP_PROGRAM!!!!!!!!!!!!!!!


if __name__ == "__main__":
    main()
