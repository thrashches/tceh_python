import json, requests, re


def read_dec(func): #output decorator
    def print_file_lines(*args, **kwargs):
        print('Your {} lines:'.format(func.__name__))
        func(*args, **kwargs)
        print('E0f')
    return print_file_lines


def write_to_file(data): #writing func
    file = open('file', 'w')
    file.write(data)
    file.close()
    print('Your data has been saved!')
    # pass


@read_dec
def read_file_data():  #reading func
    file = open('file', 'r')
    print(file.read())
    return file


########################################


#json_string = json.loads('{\n "id": 1,\n "first_name": "Guido",\n "last_name":"Rossum"\n}')
#print(json_string["id"])

@read_dec
def json_requests(url):
    data = requests.get(url)
    #if data.status_code == 200:
    print("200 OK")
    responce = data.text
    json_data = json.loads(responce, encoding="utf-8")
    for d in json_data:
        print(d["id"], d["email"])

    #print(json_data[0]["id"])
    #print(str(data.content)[7:-4])
    #print(json_str)


@read_dec
def link_parcer(url):
    responce = requests.get(url)
    if responce.status_code == 200:
        page = responce.text
        a_tags = re.findall(r'(?<=<a href=")[^"]*', page)
        for index, link in enumerate(a_tags):
            if link[0] == '/' or link[0] == '#':
                a_tags[index] = '{}/{}'.format(url, link)
        for link in a_tags: print(link)
    else:
        print("Network problems!")



write_to_file('''some string1
some string2
some string3''')

read_file_data()

json_requests('https://jsonplaceholder.typicode.com/comments')

link_parcer('http://habrahabr.ru/')