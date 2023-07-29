
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

# filename = os.listdir(root_path)
# print(filename)
def list_all_ymls(base_path):
    fileNames = next(os.walk(base_path))[2]
    # repo_list.clear()
    repo_count = 0;
    for files in fileNames:
        if files.endswith('.yml'):
            filepath = base_path + '/' + files
            with open(filepath, 'r') as file:
                prime_service = yaml.safe_load(file)
                for item in prime_service['catalog']['host']['packages']:
                    # repo_property.clear()
                    # print(files)
                    # print(item["name"])
                    if 'type' in item:
                        repo_property.append(item['name'])
                        repo_property.append(item['type'])
                        repo_property.append(
                            'https://' + prime_service['catalog']['host']['url'] + prime_service['catalog']['host'][
                                'path'] + item['name'] + '.git')
                        # repo_list[repo_count].append(item['name'])
                        # repo_list[repo_count+1].append(item['type'])
                        # repo_list[repo_count+2].append(
                        #     'https://' + prime_service['catalog']['host']['url'] + prime_service['catalog']['host'][
                        #         'path'] + item['name'] + '.git')
                        repo_count = repo_count + 3
                        # print(repo_property)
                        # print(item['type']+': ' + item['name'])
                        # print('https://' + prime_service['catalog']['host']['url'] + prime_service['catalog']['host']['path'] + item['name'] + '.git')
                    else:
                        repo_property.append(item['name'])
                        repo_property.append('NONE')
                        repo_property.append(
                            'https://' + prime_service['catalog']['host']['url'] + prime_service['catalog']['host'][
                                'path'] + item['name'] + '.git')
                        # repo_list[repo_count].append(repo_property)
                        repo_count = repo_count + 1
                        # print(repo_property)

    # display how many repositories we have
    # print(len(repo_list))

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

#
# print(len(name_list))
# print(len(url_list))
# print(len(type_list))

# count = 0
# loop = len(name_list)
# for item in range(loop):
#     if type_list[item] == 'api':
#         print(type_list[item] + ': ' + name_list[item])
#         print(url_list[item])
#         count = count + 1

# def sort_repo_by_type():
    # repo_list.sort(key=(lambda x: x[1]))



# print(prime_service)
# print(prime_service['catalog']['host']['packages'][1]['name'])
def main(argv):
    count = 0
    func_sel = ""
    repo_type = ""
    """
     通过sys模块来识别参数demo, http://blog.csdn.net/ouyang_peng/
    """
    # print('参数个数为:', len(sys.argv), '个参数。')
    # print('参数列表:', str(sys.argv))
    # print('脚本名为：', sys.argv[0])
    # for i in range(1, len(sys.argv)):
    #     print('参数 %s 为：%s' % (i, sys.argv[i]))
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

    # print('func_sel：', func_sel)
    # print('repo_type：', repo_type)

    # list_all_ymls(root_path)
    # print('Total repositories: ' + str(len(repo_property)))
    # # sort_repo_by_type()
    # repo_list = [[] for i in range(len(repo_property))]
    # print(repo_property)
    # for item in range(len(repo_property)):
    #     repo_list[item].append(repo_property[item])
    #
    # print(repo_list)
    # sys.exit()

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


    #
    # list_all_ymls(root_path)
    #
    #
    # loop = len(name_list)
    #
    # if len(sys.argv) == 2:    # print as required
    #     if (sys.argv[1] == 'api') or (sys.argv[1] == 'application') or (sys.argv[1] == 'device') or (sys.argv[1] == 'external'):
    #         for item in range(loop):
    #             if type_list[item] == sys.argv[1]:
    #                 print(type_list[item] + ': ' + name_list[item])
    #                 print(url_list[item])
    #                 count = count + 1
    #
    #     elif sys.argv[1] == 'name':
    #         for item in range(loop):
    #             print(name_list[item])
    #     else:    # print all
    #         print('Incorrect parameter, list all items.')
    #         for item in range(loop):
    #             print(type_list[item] + ': ' + name_list[item])
    #             print(url_list[item])
    #             count = count + 1
    #
    #     print('Total Repo: ' + str(count))
    # elif len(sys.argv) == 3:    # print as required
    #     if (sys.argv[1] == 'api') or (sys.argv[1] == 'application') or (sys.argv[1] == 'device') or (sys.argv[1] == 'external'):
    #         for item in range(loop):
    #             if type_list[item] == sys.argv[1]:
    #                 print(type_list[item] + ': ' + name_list[item])
    #                 print(url_list[item])
    #                 count = count + 1
    #
    #     elif sys.argv[1] == 'name':
    #         for item in range(loop):
    #             print(name_list[item])
    # else:
    #     print('Please specify api/application/device/external/all for range.')
    #     print('eg. Use below command to list all api repositories:')
    #     print('decode_catalog.py [name] [api] []')
    #     print('     decode_catalog.py api')


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])

