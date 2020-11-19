#
# Auther: zzysite
# Version: 1.0
#
# 导入os, sys模块
import os,sys
# 结束希沃PPT小工具
os.system('TASKKILL/F /IM PPTService.exe')
print('已结束希沃PPT小工具')
# 打开希沃PPT小工具
def open_app(app_dir):
  # 指定打开app方法，接收传参程序
  os.startfile(app_dir)
if __name__ == "__main__":
  # 把希沃ppt小工具赋值到变量app_dir中
  app_dir = r'C:\Program Files (x86)\Seewo\PPTService\Main\PPTService.exe'
  # 打开希沃ppt小工具
  open_app(app_dir)
  print('重启希沃PPT小工具成功')
  sys.exit()
