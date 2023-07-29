这是一套帮助下载Microchip Harmony Framework的工具
# 运行环境
python相关脚本需要python3，并安装PyYAML

## h3 下载配置工具
h3_create_new_config_github.bat  
h3_create_new_config_gitee.bat  
h3_create_config_decode_catalog.py  
### 功能和使用
从Microchip官方下载catalog文件并生成下载配置文件组*.ini
配合h3_downloader可以很方便的下载新的repo

## h3_downloader.bat h3下载工具
### 首次运行h3_downloader
1. 安装python
2. pip3 install yaml
3. 安装git客户端（步骤6#将用到）
4. 建立一个空的文件夹准备下载Harmony库文件
5. 复制./gitee中所有文件到步骤3#创建的文件夹中
6. 打开在.bat脚本，配置本地的git程序位置
7. 运行***h3_create_new_config_gitee.bat***产生分类的库列表
8. 按需要修改生成的分类.ini文件。分号开头的代表不下载，没有分号的代表需要下载
9. [可选]在命令行使用***h3_downloader.bat /demo***来检查配置文件的正确性以及是否包含了您所希望的所有内容  
10. 运行***h3_downloader.bat***下载所需的库文件

### 更新库文件
直接运行***h3_update_all.bat***会将每个库更新到最新版

### 增加新库
1. 修改对应分类的.ini文件（不用注掉已经下载的库，但是后面git会提示这个库已存在，不会产生额外问题）
2. [可选]运行***h3_downloader.bat /demo***确定需要的库已经包括
3. 运行***h3_downloader.bat***完成下载

## create_help_index.bat - 帮助文档汇总工具
功能是把各个文件夹的帮助文档汇入口总到一个网页当中
### 使用方法
- 复制create_help_index.bat和create_index_helper.bat两个文件到harmony的文件夹最外层  
- 运行***create_help_index.bat***，会在同当前文件夹生成一个help_index.html文件  
- 直接用浏览器打开可以导航到已下载库的相关帮助文档  
- 库文件有增减之后，重新运行即可重建帮助索引

## 本地管理工具
### h3_checkout_master.bat
检出本地所有仓库的master
### h3_downloader.bat
根据h3repo_*.ini文件配置，下载(git clone) 各个H3仓库
### h3_update_all.bat
更新本地所有仓库并检出master

## 依赖性助手
## h3_dependency_align.bat
根据参数指明的仓库，对齐它所要求的其他仓库版本  
Eg. h3_dependency_align.bat ./net
```
      *  Align dependency for repo - ./net
We are going to checkout repo to specify tag as below:
checkout core to v3.10.1 ...
checkout csp to v3.11.1 ...
checkout bsp to v3.11.1 ...
checkout dev_packs to v3.11.1 ...
checkout crypto to v3.7.6 ...
checkout usb to v3.8.1 ...
checkout wolfssl to v4.7.0 ...
checkout wolfMQTT to v1.11.1 ...
checkout CMSIS-FreeRTOS to v10.3.1 ...
```

## h3-dependencies-list-all.py
列出所有仓库的依赖树形。  
采用旧版xml文件描述的仓库无法提供类型和版本号，yml信息更完整。会优先使用仓库的yml文件进行解析  
```
 ├─ x,classb_sam_e5x_d5x:  
     └─ csp,3.8.2  
 ├─ x,classb_sam_e70_s70_v70_v71:  
     └─ csp,1.0.0  
 ├─ api,core,3.11.1:  
     └─ bsp,3.13.0  
     └─ csp,3.13.0  
     └─ CMSIS-FreeRTOS,10.4.6  
     └─ littlefs,2.5.0  
 ├─ application,core_apps_sam_c20_c21,v3.4.0:  
     └─ csp,v3.17.0  
     └─ dev_packs,v3.17.0  
     └─ core,v3.13.0  
 ├─ application,core_apps_sam_d5x_e5x,v3.4.0:  
     └─ csp,v3.17.0  
     └─ dev_packs,v3.17.0  
     └─ core,v3.13.0  
     └─ usb,v3.10.0  
```  