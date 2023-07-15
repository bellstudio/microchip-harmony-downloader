
import yaml
import os
import sys
import getopt

root_path = './catalog'

name_list = []
type_list = []
url_list = []

# repo_property = ['name', 'type', 'url']
repo_property = []
repo_list = []
repo_count=0

# print(prime_service)
# print(prime_service['catalog']['host']['packages'][1]['name'])
def list_all_ymls_old(base_path):
    fileNames = next(os.walk(base_path))[2]
    for files in fileNames:
        if files.endswith('.yml'):
            filepath = base_path + '/' + files
            with open(filepath, 'r') as file:
                prime_service = yaml.safe_load(file)
                for item in prime_service['catalog']['host']['packages']:
                    # print(files)
                    # print(item["name"])
                    if 'type' in item:
                        type_list.append(item['type'])
                        name_list.append(item['name'])
                        url_list.append(
                            'https://' + prime_service['catalog']['host']['url'] + prime_service['catalog']['host'][
                                'path'] + item['name'] + '.git')
                        # print(item['type']+': ' + item['name'])
                        # print('https://' + prime_service['catalog']['host']['url'] + prime_service['catalog']['host']['path'] + item['name'] + '.git')
                    else:
                        type_list.append('NONE')
                        name_list.append(item['name'])
                        url_list.append(
                            'https://' + prime_service['catalog']['host']['url'] + prime_service['catalog']['host'][
                                'path'] + item['name'] + '.git')


        # packages:
        #     - name: "crypto"
        #       title: "Harmony 3 - Cryptography solutions"
        #       package_group: "Harmony 3 Crypto solutions"
        #       type: "api"
        #       category: "cryptography"
        #       required: "false"
        #       tag-check: true
        #       package-check: true
        #       third_party: false


def main(argv):
    count = 0
    func_sel = ""
    repo_type = ""
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:t:", ["help", "function=", "type="])
    except getopt.GetoptError:
        print('Error: test_arg.py -f <function type> -t <repo type>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('test_arg.py -f <function type> -t <repo type>')
            print('or: test_arg.py --function=<functions to proceed> --type=<repo type>')
            print(' function: name, name_type, url, all')
            print(' type: api, application, devices, tool, documentation, external, all')
            sys.exit()
        elif opt in ("-t", "--type"):
            repo_type = arg
        elif opt in ("-f", "--func"):
            func_sel = arg

    list_all_ymls_old(root_path)
    
    print(';; define content name in below')
    print(';; one item a line')
    print(';;===============================')

    loop = len(name_list)
    for item in range(loop):
        if (type_list[item] == repo_type) or (repo_type == 'all') or (repo_type == ''): # select repo
            if func_sel == 'name':  # select different print out
                print(name_list[item])
                # print(url_list[item])
                count = count + 1
            elif func_sel == 'name_type':  # select different print out
                print(type_list[item] + ': ' + name_list[item])
                # print(url_list[item])
                count = count + 1
            elif func_sel == 'name_url':  # select different print out
                print(name_list[item] + ',' + url_list[item])
                count = count + 1
            elif func_sel == 'configfile':  # select different print out
                print(';'+name_list[item] + ',' + url_list[item])
                count = count + 1
            elif func_sel == 'url':  # select different print out
                # print(type_list[item] + ': ' + name_list[item])
                print(url_list[item])
                count = count + 1
            else:  # select different print out
                print(type_list[item] + ': ' + name_list[item])
                print(url_list[item])
                count = count + 1


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])

