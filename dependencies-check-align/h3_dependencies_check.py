from pathlib import Path
import yaml
import xml.etree.ElementTree as ET
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

def check_dependency_yml(r_name):
    filepath = Path(r_name)
    if filepath.is_dir() == False:
        print('ERROR: wrong path')
        return
    filepath = Path(str(r_name)+'/'+'package.yml')
    xfilepath = Path(str(r_name)+'/'+'package.xml')
    # print(filepath.exists())
    if filepath.exists():
        with open(filepath, 'r') as file:
            prime_service = yaml.safe_load(file)
            if 'dependencies' in prime_service['package']:
                for item1 in prime_service['package']['dependencies']:
                    if item1['type'] == 'package':	# avoid list all DFP details
                        if item1['version'].startswith("v"):
                            print(item1['name'] + ',' + item1['version'])
                        else:
                            print(item1['name'] + ',' + 'v' + item1['version'])
    elif xfilepath.exists():
        print(';; yml file not exist')
        print(';; xml file used instead')
        tree = ET.parse(xfilepath)
        root = tree.getroot()
        for dependency in root.iter('Dependency'):
            print(dependency.get('name') + ',' + dependency.get('version'))
    else:
        print('ERROR: package.yml/package.xml do not exist.')


def main(argv):
    count = 0
    repo_type = ""
    func_sel = 'all'
    repo_name = ''

    """
     通过sys模块来识别参数demo, http://blog.csdn.net/ouyang_peng/
    """
    # print('参数个数为:', len(sys.argv), '个参数。')
    # print('参数列表:', str(sys.argv))
    # print('脚本名为：', sys.argv[0])
    # for i in range(1, len(sys.argv)):
    #     print('参数 %s 为：%s' % (i, sys.argv[i]))
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:", ["help", "name="])
    except getopt.GetoptError:
        print('Error: test_arg.py -f <function type> -t <repo type>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('dependencies-check.py -n <repo path>')
            print('or: dependencies-check.py --name=<repo path to proceed>')
            print(' name: full or relative path of repo be checked')
            print('eg.: dependencies-check.py -n ./usb')
            sys.exit()
        elif opt in ("-n", "--name"):
            repo_name = arg

    print(';; ' + repo_name)
    print(';; define content name in below')
    print(';; one item a line')
    print(';;===============================')
#    list_dependency_ymls(func_sel)
    check_dependency_yml(repo_name)

if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])

