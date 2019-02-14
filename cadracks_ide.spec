# -*- mode: python -*-

# run 'pyintaller cadracks_ide.spec' from the cadracks-ide root project folder

block_cipher = None

added_files = [("cadracks_ide/cadracks-ide.ico", "."),
               ("cadracks_ide/cadracks-ide.ini", "."),
               ("cadracks_ide/icons/*", "icons"),
               ("../../guillaume-florent/aoc-utils/aocutils/display/icons/*", "aocutils/display/icons")]


a = Analysis(['cadracks_ide/cadracks_ide_ui.py'],
             pathex=['/home/guillaume/_Repositories/github/cadracks/cadracks-ide'],
             binaries=[],
             datas=added_files,
             hiddenimports=['cadracks_core.joints', 'ccad', 'ccad.model'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='cadracks-ide',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='cadracks-ide')
