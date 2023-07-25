import yaml
import os
import sys
import getopt

root_path = '.'

name_list = []
type_list = []
url_list = []

# repo_property = ['name', 'type', 'url']
repo_property = []
repo_list = []
repo_count = 0


def list_dependency_ymls(pack_type):
    dirs = next(os.walk("."))[1]
    for dir in dirs:
        # print(dir)
        fileNames = next(os.walk("./" + dir))[2]
        for files in fileNames:
            if files == 'package.yml':
                filepath = './' + dir + '/' + files
                # print(filepath)
                with open(filepath, 'r') as file:
                    prime_service = yaml.safe_load(file)
                    if 'dependencies' in prime_service['package']:
                        if pack_type == 'all':
                            if 'type' in prime_service['package']:
                                print(prime_service['package']['type'] + ',' + prime_service['package']['name'] + ',' +
                                      prime_service['package']['version'] + ':')
                            else:
                                print('None' + ',' + prime_service['package']['name'] + ',' + prime_service['package'][
                                    'version'] + ':')
                            for item1 in prime_service['package']['dependencies']:
                                if item1['type'] == 'package':
                                    print('  *' + item1['name'] + ',' + item1['version'])
                        else:
                            if pack_type.startswith('-'):
                                pack_type_check = pack_type[1:]
                                if 'type' in prime_service['package']:
                                    if pack_type_check != prime_service['package']['type']:
                                        print(prime_service['package']['name'] + ',' + prime_service['package'][
                                            'version'] + ':')
                                        for item1 in prime_service['package']['dependencies']:
                                            if item1['type'] == 'package':
                                                print('  *' + item1['name'] + ',' + item1['version'])
                                else:
                                    print(
                                        prime_service['package']['name'] + ',' + prime_service['package']['version'] + ':')
                                    for item1 in prime_service['package']['dependencies']:
                                        if item1['type'] == 'package':
                                            print('  *' + item1['name'] + ',' + item1['version'])
                            else:
                                if 'type' in prime_service['package']:
                                    if pack_type == prime_service['package']['type']:
                                        print(prime_service['package']['name'] + ',' + prime_service['package'][
                                            'version'] + ':')
                                        for item1 in prime_service['package']['dependencies']:
                                            if item1['type'] == 'package':
                                                print('  *' + item1['name'] + ',' + item1['version'])

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
    func_sel = 'all'

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
            if repo_type == 'app':
                func_sel = 'application'
            elif repo_type == 'lib':
                func_sel = 'package'
            elif repo_type == 'api':
                func_sel = 'api'
            if repo_type == '-app':
                func_sel = '-application'
            elif repo_type == '-lib':
                func_sel = '-package'
            elif repo_type == '-api':
                func_sel = '-api'
        elif opt in ("-f", "--func"):
            func = arg
            if func == 'app':
                func_sel = 'application'
            elif func == 'lib':
                func_sel = 'package'
            elif func == 'api':
                func_sel = 'api'

    print(';; define content name in below')
    print(';; one item a line')
    print(';;===============================')
    list_dependency_ymls(func_sel)


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])

