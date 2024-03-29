import requests , os , sys , click
from lxml import html

os.system("")

class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'

RPGURL_LOGIN = "https://rapidgator.net/api/v2/user/login"
RPGURL_FILEINFO = "https://rapidgator.net/api/v2/file/info/"

@click.command()
@click.option('--username', '-u' , 'USERNAME', required=True)
@click.option('--password', '-p' , 'PASSWORD', required=True)
@click.option('--filelist', '-f' , 'LISTOFDOWNLOAD', required=True)
def rapidstatus(USERNAME , PASSWORD , LISTOFDOWNLOAD):
    #Validate
    if not os.path.exists(LISTOFDOWNLOAD) and os.path.isfile(LISTOFDOWNLOAD) :
        print ("List of download url not exist")
        sys.exit(0)


    PARAMS = {"login": USERNAME, "password": PASSWORD}

    r = requests.get(url=RPGURL_LOGIN, params=PARAMS)
    data = r.json()
    token = data["response"]["token"]

    with open(LISTOFDOWNLOAD) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            #print("File {}: {}".format(cnt, line.strip()))
            file_name = None
            _url = line.strip()

            if not _url :
                print("++END++")
                sys.exit(0)

            _file_id = _url.split("/")[4]

            url = RPGURL_FILEINFO
            params = {"file_id": _file_id, "token": token}
            r = requests.get(url=url, params=params)
            data = r.json()
            status = style.GREEN + "Link is Alive" if data["status"] == 200 else style.RED + "Link was dead/wrong"
            print("File {}: {} -> {} {}".format(cnt, line.strip(), status, style.RESET))
            line = fp.readline()
            cnt += 1

if __name__ == '__main__':
    rapidstatus()
