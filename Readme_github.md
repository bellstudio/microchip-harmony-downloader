# This is a set of scripts help manage Microchip Harmony Framework
## Run time environment
 - Python 3.x  
 - PyYaml

## h3 dowload configurator
h3_create_new_config_github.bat  
h3_create_new_config_gitee.bat  
h3_create_config_decode_catalog.py  
### Fucntion and usage
Download official H3 catalog file and put repo names and address in *.ini files per type.
All content is comment out(with comma in front) by default
Uncomment those content you want to download
Work with h3_downloader to get those content

## h3_downloader.bat h3 download helper
### first time running h3_downloader
1. Install python 3.x
2. use "pip3 install yaml" to install PyYaml
3. Install Git-scm(will be used at step6)
4. Prepare a empty folder you H3 content will be placed
5. copy `*.ini files created by ***h3 dowload configurator***
6. open h3_downloader.bat in editor，set the ***gitpath*** according to your system
7. [opt]use***h3_downloader.bat /demo*** in command line to check contents are going to be downloaded  
8. run ***h3_downloader.bat*** to get all you want

### Update H3 local libraries
run ***h3_update_all.bat*** 

### Add new lib
1. Modify *.ini file to include new lib（comment out the old ones is optional, if old ones are listed, git will promote a warning - ignore them）
2. [opt]use***h3_downloader.bat /demo*** in command line to check contents are going to be downloaded 
3. run ***h3_downloader.bat*** to get all you want

## create_help_index.bat - Help file collector
Create an unique entrance of all downloaded H3 libs help
### Usage
- copy create_help_index.bat and create_index_helper.bat to the root of Harmony libraries  
- run ***create_help_index.bat***，will get a help_index.html file
- run script again if new libs added

## local management helper
### h3_checkout_master.bat
checkout all libs to master. when start a new project, this is a good start.
### h3_downloader.bat
Harmony libs download helper
### h3_update_all.bat
update all local libs and checkout to master

## H3 dependency helper
## h3_dependency_align.bat
read library dependency file and align other related libs version to the library we specified
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
list all local libs dependency tree
will decode yml dependency file in priority, if yml doesn't exist, will try to decode xml file
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