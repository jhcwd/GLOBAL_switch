import os

def switch():
    local = os.getcwd()
    localglobaldata = local + '\\GLOBALDATA'
    #print(localglobaldata)
    globallist = os.listdir(localglobaldata)
    print('请选择所需要切换的global：')
    for i in range (0,len(globallist)):
        output = '【' + str(i) + '】 ' + globallist[i]
        print(output)
    global_swich = input()
    command = 'mklink /D '
    command += (local + '\\GLOBAL' + ' ' + localglobaldata + '\\' + globallist[int(global_swich)])
    #print(command)

    os.system('rmdir /S /Q GLOBAL')
    os.system(command)
    print('切换成功')




print('欢迎使用GLOBAL切换器！\n！！！重要：请使用管理员权限运行本程序')
print('使用说明：请将每个线路GLOBAL文件夹放在本程序目录下的GLOBALDATA文件夹内，名字可以任意')
while(1):
    print('菜单：\n【0】切换GLOBAL\n【1】退出')
    inmenu = input('请输入指令：')
    if(inmenu == '1'):
        break
    elif(inmenu== '0'):
        switch()



