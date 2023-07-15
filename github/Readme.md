这是一套帮助下载Microchip Harmony Framework的工具

# 运行环境：
## 首次运行：
1. 安装python
2. pip3 install yaml
3. 安装git客户端
3. 在.bat脚本中配置本地的git程序位置
4. 复制所有文件到Harmony3库所在文件夹
5. 运行***h3_create_new_config_github.bat***产生分类的库列表
6. 修改生成的分类.ini文件。分号开头的代表不下载，没有分号的代表需要下载
7. [可选]在命令行使用***h3_downloader.bat /demo***来检查配置文件的正确性以及是否包含了您所希望的所有内容
8. 运行***h3_downloader.bat***下载所需的库文件

## 更新库文件：
直接运行***h3_update_all.bat***会更新到最新版

## 增加新库
1. 修改对应分类的.ini文件（可以不用注掉已经下载的库，但是后面git会提示这个库已存在）
2. [可选]运行***h3_downloader.bat /demo***确定需要的库已经包括
3. 运行***h3_downloader.bat***完成下载