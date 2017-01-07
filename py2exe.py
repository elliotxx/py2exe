# coding=gbk

# py2exe
# 作者：freecode
# 创建时间：2016/5/11 10:54
# 作用：
#   将python脚本转换成windows下exe可执行文件
# 执行条件：
#   1、pyInstall已安装，安装目录在.\InstallPackage目录下
#   2、pywin32-220.win32-py2.7.exe已安装
#   3、所在目录必须为中文
#

import os
import shutil
import sys

class Py2Exe:
   def py2exe(self,argv=None):
        if argv==None:
            FileName = raw_input('请输入待转换py文件名称（必须在当前目录下）：').strip()
        else:
            FileName = argv[1].strip()
            
        if FileName[0]=='\"' or FileName[0]=='\'':   # 去除引号
            FileName = FileName[1:-1]
        FileName = FileName.split('\\')[-1]    # 截取文件名
        
        # 生成exe文件
        CurrentPath = os.getcwd()       
        PyInstaller = sys.path[0]+"\\InstallPackage\\PyInstaller-3.1.1\\pyinstaller.py"   # 安装器位置
        PyFile_1 = sys.path[0]+'\\'+FileName              # 转换文件
        SpecFile = CurrentPath+'\\'+FileName[:-3]+'.spec'     # 要删除的spec文件
        ExeFile_1 = "%s.exe"%(FileName[:-3])        # 生成的exe文件名
        ExePath_1 = "%s\\dist\\%s"%(CurrentPath,ExeFile_1)  # exe文件所在目录
        CopyPath_1 = "%s\\%s"%(CurrentPath,ExeFile_1)        # exe文件复制目录

        if os.path.exists(sys.path[0]+'\\'+ExeFile_1):
            print "%s已存在，不需要转换"%(ExeFile_1)
            return False
        else:
            # 转换开始
            os.system('python "%s" --console --onefile "%s"'%(PyInstaller,PyFile_1))


        # 移动exe文件，删除多余文件

        if os.path.exists(ExePath_1):
            print 'exe生成完毕'
            print '复制文件%s到%s……' % (ExePath_1,CopyPath_1)
            shutil.copy(ExePath_1,CopyPath_1)
            if argv != None:
                print '复制文件%s到%s……' % (CopyPath_1,sys.path[0]+'\\'+ExeFile_1)
                shutil.move(CopyPath_1,sys.path[0]+'\\'+ExeFile_1)
        else:
            print 'exe生成失败'
            print '文件%s不存在'%(ExePath_1)
            return False
            
        if os.path.exists(CurrentPath+"\\dist"):
            print '删除目录%s……' % (CurrentPath+"\\dist")
            shutil.rmtree(CurrentPath+"\\dist")
        else:
            print '目录%s不存在'%(CurrentPath+"\\dist")
            return False

        if os.path.exists(CurrentPath+"\\build"):
            print '删除目录%s……' % (CurrentPath+"\\build")
            shutil.rmtree(CurrentPath+"\\build")
        else:
            print '目录%s不存在'%(CurrentPath+"\\build")
            return False

        if os.path.exists(SpecFile):
            print '删除文件%s……' % (SpecFile)
            os.remove(SpecFile)
        else:
            print '文件%s不存在'%(SpecFile)
            return False
        return True
            
        
if __name__=='__main__':
    # 判断是否是在直接运行该.py文件
    if len(sys.argv)==1:
        Py2Exe().py2exe()
    elif len(sys.argv)==2:
        Py2Exe().py2exe(sys.argv)
    else:
        print 'ERROR:参数错误!\n'
    raw_input('\n请按回车键(Enter)退出……')

    

