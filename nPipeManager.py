import maya.cmds as mc


class NPipeManager(object):
    def __init__(self):
        hoge = ''

    def ui(self, *args):
        managewin = mc.window('managewin', t='nPipe Manager', widthHeight=(400,200))

        menuBarLayout = mc.menuBarLayout()
        mc.menu(label='File')
        mc.menuItem(label='Setting')

        mc.menu(label='Help', helpMenu=True)
        mc.menuItem(label='About...')

        form = mc.formLayout()

        # 初期プロジェクトディレクトリ生成
        # アセット登録
        # ショット登録
        # ユーザ登録


        mc.showWindow(managewin)


b = NPipeManager()
b.ui()