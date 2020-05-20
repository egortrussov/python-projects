import requests
import html2text


def get_request(url):
    req_get = requests.get(url)
    cont = unicode(req_get.content, "utf-8")
    if len(cont) == 0:
        if req_get.status_code == 200:
            print (html2text.html2text(cont))
        elif req_get.status_code == 404:
            print ("Error 404, Not Found!")
        elif req_get.status_code == 500:
            print ("Error 500, Internal server error!")
        else:
            print (html2text.html2text(cont))

    else:
        print (html2text.html2text(cont))


def main():

    while True:
        link = input("URL: ")
        if link == "quit":
            break
        else:
            pass

        get_request(link)


if __name__ == "__main__":
    main()