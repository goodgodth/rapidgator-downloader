import requests , os , sys , click
from lxml import html

RPGURL_LOGIN = "https://rapidgator.net/api/v2/user/login"
#RPGURL_FILEINFO = "https://rapidgator.net/api/v2/file/info/"
RPGURL_FILEDOWNLOAD = "https://rapidgator.net/api/v2/file/download/"
RPG_XPATH_FILENAME = "//div[@class='text-block file-descr']//p//a//text()"

@click.command()
@click.option('--username', '-u' , 'USERNAME', required=True)
@click.option('--password', '-p' , 'PASSWORD', required=True)
@click.option('--url', '-url' , 'RAPIDURL', required=True)
@click.option('--savedirectory', '-d' , 'PATH', required=True)
def rapiddownload(USERNAME , PASSWORD , RAPIDURL , PATH):
    #Validate
    if not os.path.exists(PATH) and os.path.isdir(PATH) :
        print ("Save Directory not exist")
        sys.exit(0)


    PARAMS = {"login": USERNAME, "password": PASSWORD}

    r = requests.get(url=RPGURL_LOGIN, params=PARAMS)
    data = r.json()
    print("data : " + str(data))
    token = data["response"]["token"]


    file_name = None
    file_name_alt = None

    _file_id = RAPIDURL.split("/")[4]

    ## If want assign filename from URL (htttp://rg.to/408320/assign_filename_by_yourself.rar ==> file_name = assign_filename_by_yourself.rar
    # try:
    #     file_name = _url.split("/")[5]
    #     file_name = file_name.replace(".html", "")
    #     print("expect file name : " + file_name)
    # except:
    #     print("file name not found")
    #     file_name = str(int(round(time.time() * 1000)))
    ## end If

    ## If want get filename from original uploader
    page = requests.get(RAPIDURL)
    print(page.status_code)
    if page.status_code > 400 :
        print("URL : "+str(RAPIDURL)+ "get HTTP STATUS "+str(page.status_code))
        file_name = _file_id
    else :
        root = html.fromstring(page.text)
        tree = root.getroottree()
        result = root.xpath(RPG_XPATH_FILENAME)
        file_name = ''.join([word.strip() for word in result])
        file_name = len(file_name) > 0 and file_name or _file_id
        if file_name_alt is not None:
            file_name = file_name_alt
        file_name = file_name.encode('ascii', 'ignore')
        if not file_name :
            file_name = _file_id
        if os.path.exists(str(PATH) + "/" + str(file_name)) :
            file_name = _file_id
    ## end IF

    url = RPGURL_FILEDOWNLOAD
    params = {"file_id": _file_id, "token": token}
    r = requests.get(url=url, params=params)
    data = r.json()
    print(data)
    _dl_url = data["response"]["download_url"]
    print("Response :" + str(data) + " \ngetDownloadLink : " + str(_dl_url))
    download_cmd = "wget -P " + str(PATH) + " -O '" +str(PATH) + "/" + str(file_name, 'utf-8') + "' '" + str(_dl_url) + "'"

    print(download_cmd)
    os.system(download_cmd)

if __name__ == '__main__':
    rapiddownload()
