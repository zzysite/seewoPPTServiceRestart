#
# Auther: zzysite
# Version: 1.1
# changelog: 更改获取安装路径的方式为注册表，
# 防止本程序在其他目录下安装的希沃PPT小工具的环境下不起作用
#

# 导入os, sys, winreg模块
import os, sys, winreg

# 结束希沃PPT小工具
os.system('TASKKILL/F /IM PPTService.exe')
print('已结束希沃PPT小工具')

# 从注册表中获取希沃PPT小工具的安装路径
def getSeewoPPTServiceWhere ():
  string = r'SOFTWARE\WOW6432Node\Seewo\PPTService'
  handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, string, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
  location, _type = winreg.QueryValueEx(handle, "ExePath")
  return location

# 打开希沃PPT小工具
def open_app(app_dir):
  # 指定打开app方法，接收传参程序
  os.startfile(app_dir)
if __name__ == "__main__":
  # 把希沃ppt小工具赋值到变量app_dir中
  app_dir = getSeewoPPTServiceWhere()
  # 打开希沃ppt小工具
  open_app(app_dir)
  print('重启希沃PPT小工具成功')
  sys.exit()
