这是一套帮助下载Microchip Harmony Framework的工具

# h3_downloader运行环境
## 首次运行h3_downloader
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

## 更新库文件
直接运行***h3_update_all.bat***会将每个库更新到最新版

## 增加新库
1. 修改对应分类的.ini文件（不用注掉已经下载的库，但是后面git会提示这个库已存在，不会产生额外问题）
2. [可选]运行***h3_downloader.bat /demo***确定需要的库已经包括
3. 运行***h3_downloader.bat***完成下载

# create_help_index.bat - 帮助文档汇总工具
功能是把各个文件夹的帮助文档汇入口总到一个网页当中
## 使用方法
- 复制create_help_index.bat和create_index_helper.bat两个文件到harmony的文件夹最外层  
- 运行***create_help_index.bat***，会在同当前文件夹生成一个help_index.html文件  
- 直接用浏览器打开可以导航到已下载库的相关帮助文档  
- 库文件有增减之后，重新运行即可重建帮助索引