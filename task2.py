from pprint import pprint

import requests
from ya_disk import YandexDisk
TOKEN = ""

if __name__ == '__main__':
    yd = YandexDisk(token=TOKEN)
    # pprint(yd.get_files_list())
    # filt_list =yd.get_files_list()
    pprint(yd.upload_file_to_disk("netology/test.txt",'1\khg.txt'))