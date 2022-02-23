# Rapidgator-Downloader
Download file from rapidgator with premium user

## rapidgatorstatus.py
Download by read list of URL in text file (Example : dl.txt)

### How to run
```sh
Usage: rapidgatorstatus.py [OPTIONS]

Options:
  -u, --username TEXT  [required]
  -p, --password TEXT  [required]
  -f, --filelist TEXT  [required]
  --help               Show this message and exit.
```

### Example
```sh
$ python rapidgatorstatus.py --username noeybnk48@gmail.com --password noeyBNK48 --directory /home/noeybnk48/dl.txt

$ python rapidgatorstatus.py --username noeybnk48@gmail.com --password noeyBNK48 --directory /home/noeybnk48/dlwithrename.txt

```


## rapidgatordl.py
Download by read list of URL in text file (Example : dl.txt)

### How to run
```sh
Usage: rapidgatordl.py [OPTIONS]

Options:
  -u, --username TEXT       [required]
  -p, --password TEXT       [required]
  -f, --filelist TEXT       [required]
  -d, --savedirectory TEXT  [required]
  --help                    Show this message and exit.
  ```

### Example
```sh
$ python rapidgatordl.py --username noeybnk48@gmail.com --password noeyBNK48 --directory /home/noeybnk48/download/ --filelist /home/noeybnk48/dl.txt

$ python rapidgatordl.py --username noeybnk48@gmail.com --password noeyBNK48 --filelist /home/noeybnk48/dlwithrename.txt --directory /home/noeybnk48/download/

```


## rapidgatorsingle.py
Download by URL in argument

### How to run

```sh
Usage: rapidgatorsingle.py [OPTIONS]

Options:
  -u, --username TEXT       [required]
  -p, --password TEXT       [required]
  -url, --url TEXT          [required]
  -d, --savedirectory TEXT  [required]
  --help                    Show this message and exit.
```

### Example
```sh
$ python rapidgatorsingle.py --username noeybnk48@gmail.com --password noeyBNK48 --url https://rg.to/file/x318300757fa8c7234e9b837431efa5186  --directory /home/noeybnk48/download/

```

###

---


### Reference

 - [Rapidgator API](https://rapidgator.net/article/api/index).
