import sys

issue = {
    'name': "", 'surname': "", 'email': "", 'location': "", 'query': ""
}


def skip(string_val, line, src):
    while line.find(string_val) == -1:
        line = src.readline()
    return line, src


def from_form():
    src = open("read.txt", 'r')
    line = src.readline()
    
    for _ in range(4):
        while line != "=============================\n":
            line = src.readline()
        line = src.readline()
    for val in ['name', 'surname', 'email']:
        line = src.readline()
        issue[val] = line.split('=')[1].replace("\n", "")

    line, src = skip('C_Zip_Postal=')

    line = src.readline()
    issue['location'] = line.split('=')[1].replace("\n", "")

    line, src = skip('UDF_01_Question=')

    chungus = []

    while line.find("A_Timestamp=") == -1:
        line = line.split("=")[1]
        chungus.append(line.replace("\n", ""))
        line = src.readline().replace("\n", "")

    clean_chung = []
    for _ in chungus:
        if len(_) == 0:
            continue
        clean_chung.append(_)

    super_clean_chung = ""
    for _ in clean_chung:
        _.replace('\n', "")
        super_clean_chung += _
        super_clean_chung += '\n'

    issue['query'] = super_clean_chung
    src.close()


def from_third_party():
    src = open('read.txt', 'r')

    line = src.readline()

    while line.find("First Name") == -1:
        line = src.readline()

    for val in ['name', 'surname', 'email']:
        line = src.readline().split(" ")[1].replace('\n', '')
        issue[val] = line
        line = src.readline()

    line, src = skip('*C_Country*')

    line = src.readline()
    issue['location'] = line[2::]

    line, src = skip('UDF_01_Question')
    line = src.readline()

    chungus = []

    while line.find("A_Timestamp") == -1:
        line.replace("\n", '')
        if line.find('*') == 2:
            line = src.readline().replace('\n', '')
            continue
        else:
            chungus.append(line[2::].replace('\n', ''))

        line = src.readline()

    clean_chung = ""
    for _ in chungus:
        clean_chung += _ + '\n'

    issue['query'] = clean_chung
    src.close()


def read_file(var):
    match var:
        case "1":
            from_form()
        case "2":
            from_third_party()


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("wrongly executed")
        print("correct should be:\n$ python readable.py <1/2>\nnumber represents version of the text\n1 - direct from form\n2-from third party")
        exit(1)

    read_file(sys.argv[1])

    # print(issue)

    print("-------> NAME: ", end="")
    print(issue['name'])

    print("--> SURNAME: ", end="")
    print(issue['surname'])

    print("-------> EMAIL: ", end="")
    print(issue['email'])

    print("--> LOCATION: ", end="")
    print(issue['location'])

    print()
    print("----------------")
    print("QUERY:")
    print("----------------")
    print()

    print(issue['query'])
