# -*- mode: python -*-
a = Analysis(['rtspdeal.py'],
             pathex=[],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'rtspdeal.exe'),
          debug=False,
          strip=None,
          upx=False,
          console=True , icon='rtspdeal.ico')
