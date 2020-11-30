# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
#//'PreTestQuestions.txt','PreTestAnswers.txt','profileMaker.txt','subjectSelector.txt','mp_profile.txt','Level3Questions.txt','Level3Answers.txt','Level2Questions.txt','Level2Answers.txt','Level1Questions.txt','Level1Answers.txt','funsmart.png','funsmart1.png','bottom.png','bg.png','FunSmar_main.py'

a = Analysis(['login.py','Methods.py','PreTest.py','Home.py','GameBoard.py',],
             pathex=['D:\\Courses_the longer the better then it can be seem easily~~hahahahaha\\Software Engineering\\project\\1128\\FunSmart'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='login',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='login')
