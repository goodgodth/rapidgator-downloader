import requests
import os
import sys

URL = "https://rapidgator.net/api/v2/user/login"

PARAMS = {"login": sys.argv[1], "password": sys.argv[2]}

PATH = sys.argv[3]

r = requests.get(url=URL, params=PARAMS)
data = r.json()
print("data : " + str(data))
token = data["response"]["token"]
print("data : " + str(data) + "\ntoken : " + token)

with open(sys.argv[4]) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("File {}: {}".format(cnt, line.strip()))
        file_name = None
        _url = line.strip()
        _file_id = _url.split("/")[4]
        try:
            file_name = _url.split("/")[5]
            file_name = file_name.replace(".html", "")
            print("expect file name : " + file_name)
        except:
            print("file name not found")
        url = "https://rapidgator.net/api/v2/file/info/"
        params = {"file_id": _file_id, "token": token}
        print("GET method TO URL : " + str(url) + " with param " + str(params))
        r = requests.get(url=url, params=params)
        data = r.json()

        print("Response :" + str(data) + " \nFile name : ")
        try:
            file_name = data["response"]["link"]["file"]["name"]
        except:
            print("file name not found")
        # print(
        #     "File ID : "
        #     + _file_id
        #     + " -> "
        #     + data["result"]["files"][_file_id]["status"]
        # )
        # if file_status == 200:
        url = "https://rapidgator.net/api/v2/file/download/"
        params = {"file_id": _file_id, "token": token}
        r = requests.get(url=url, params=params)
        data = r.json()
        _dl_url = data["response"]["download_url"]
        print("Response :" + str(data) + " \ngetDownloadLink : " + str(_dl_url))
        if file_name == None:
            os.system("wget -P " + PATH + " -O " + _file_id + " '" + _dl_url + "'")
        else:
            os.system("wget -P " + PATH + " -O " + file_name + " '" + _dl_url + "'")
        line = fp.readline()
        cnt += 1
