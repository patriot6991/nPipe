import maya.cmds as mc
import urllib2
import json

class NPipe(object):
    def __init__(self):
        self.json = ''
        self.assets = []
        self.asset = ''
        self.LoDs = []
        self.versions = []
        self.note = ''

    def getAsset(self, *args):
        f = open('C:/hoge.json', 'r')
        self.json = json.load(f)
        self.assets = self.json['asset'].keys()

    def getLoD(self, asset, *args):
        self.LoDs = []
        self.asset = asset
        self.LoDs = self.json['asset'][asset].keys()
        mc.textScrollList('m_l2', ra=True, append=self.LoDs, edit=True, enable=True)

    def getVersion(self, LoD, *args):
        self.versions = []
        self.versions = self.json['asset'][self.asset][LoD].keys()
        mc.textScrollList('m_l3', ra=True, append=self.versions, edit=True, enable=True)

    def selectNode(self, scrollList, *args):
        selectedNode = mc.textScrollList(scrollList, query=True, selectItem=True)
        if scrollList == 'm_l1':
            self.getLoD(selectedNode[0])
        else:
            self.getVersion(selectedNode[0])


    def ui(self, *args):
        win = mc.window('win', t='nPipe')

        menuBarLayout = mc.menuBarLayout()
        mc.menu(label='File')
        mc.menuItem(label='Setting')

        mc.menu(label='Help', helpMenu=True)
        mc.menuItem(label='About...')

        tab = mc.tabLayout(imw=5, imh=5, w=795, h=505)

        # -----------------------------------------------------------
        tab1 = mc.formLayout()
        m_t1 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        m_l1 = mc.textScrollList('m_l1', w=120, h=200, append=self.assets, selectCommand=lambda: self.selectNode('m_l1'))
        m_t2 = mc.text(l=' LoD:', al='left', w=200, h=20)
        m_l2 = mc.textScrollList('m_l2', w=120, h=200, append=self.LoDs, selectCommand=lambda: self.selectNode('m_l2'))
        m_t3 = mc.text(l=' Version:', al='left', w=200, h=20)
        m_l3 = mc.textScrollList('m_l3', w=120, h=200)
        m_t4 = mc.text(l=' Note:', al='left', w=200, h=20)
        m_s1 = mc.scrollField(text='hoge', w=380, h=200)
        m_b1 = mc.button(l='import', w=80, h=25)
        m_t5 = mc.text(l='Directory:', al='right', w=60, h=25)
        m_f1 = mc.textField(text='directory', w=520, h=25)
        m_b2 = mc.button(l='open', w=80, h=25)

        m_sp = mc.separator(w=790)

        m_t6 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        m_o1 = mc.optionMenu(w=120, h=25)
        m_t7 = mc.text(l=' LoD:', al='left', w=200, h=20)
        m_o2 = mc.optionMenu(w=120, h=25)
        m_t8 = mc.text(l=' Status:', al='left', w=200, h=20)
        m_o3 = mc.optionMenu(w=120, h=25)
        m_b3 = mc.button(l='Publish!!', w=380, h=50)
        m_t9 = mc.text(l=' Note:', al='left', w=200, h=20)
        m_s2 = mc.scrollField(text='hoge', w=380, h=85)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab2 = mc.formLayout()
        mc.setParent('..')

        # -----------------------------------------------------------
        tab3 = mc.formLayout()
        pr_o1 = mc.optionMenu(w=120, h=25)
        pr_t1 = mc.text(l=' Shot:', al='right', w=60, h=20)
        pr_o2 = mc.optionMenu(w=120, h=25)
        pr_t2 = mc.text(l=' Cut:', al='right', w=60, h=20)
        pr_t3 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        pr_l1 = mc.textScrollList(w=120, h=200)
        pr_t4 = mc.text(l=' LoD:', al='left', w=200, h=20)
        pr_l2 = mc.textScrollList(w=120, h=200)
        pr_t5 = mc.text(l=' Version:', al='left', w=200, h=20)
        pr_l3 = mc.textScrollList(w=120, h=200)
        pr_t6 = mc.text(l=' Note:', al='left', w=200, h=20)
        pr_s1 = mc.scrollField(text='hoge', w=380, h=200)
        pr_b1 = mc.button(l='import', w=80, h=25)
        pr_t7 = mc.text(l='Directory:', al='right', w=60, h=25)
        pr_f1 = mc.textField(text='directory', w=520, h=25)
        pr_b2 = mc.button(l='open', w=80, h=25)

        pr_sp = mc.separator(w=790)

        pr_t8 = mc.text(l=' Shot:', al='left', w=200, h=20)
        pr_o3 = mc.optionMenu(w=120, h=25)
        pr_t9 = mc.text(l=' Cut:', al='left', w=200, h=20)
        pr_o4 = mc.optionMenu(w=120, h=25)
        pr_t10 = mc.text(l=' Status:', al='left', w=200, h=20)
        pr_o5 = mc.optionMenu(w=120, h=25)
        pr_t11 = mc.text(l=' Note:', al='left', w=200, h=20)
        pr_s2 = mc.scrollField(text='hoge', w=335, h=45)
        pr_b3 = mc.button(l='Publish Camera!!', w=380, h=50)

        pr_t12 = mc.text(l=' Shot:', al='left', w=200, h=20)
        pr_o6 = mc.optionMenu(w=120, h=25)
        pr_t13 = mc.text(l=' Cut:', al='left', w=200, h=20)
        pr_o7 = mc.optionMenu(w=120, h=25)
        pr_t14 = mc.text(l=' Status:', al='left', w=200, h=20)
        pr_o8 = mc.optionMenu(w=120, h=25)
        pr_t15 = mc.text(l=' Note:', al='left', w=200, h=20)
        pr_s3 = mc.scrollField(text='hoge', w=335, h=45)
        pr_b4 = mc.button(l='Publish Image!!', w=380, h=50)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab4 = mc.formLayout()
        mc.setParent('..')

        # -----------------------------------------------------------
        tab5 = mc.formLayout()
        mc.setParent('..')

        # -----------------------------------------------------------
        tab6 = mc.formLayout()
        mc.setParent('..')

        # -----------------------------------------------------------
        tab7 = mc.formLayout()
        mc.setParent('..')

        # -----------------------------------------------------------
        tab8 = mc.formLayout()
        mc.setParent('..')

        # -----------------------------------------------------------
        tab9 = mc.formLayout()
        mc.setParent('..')

        mc.tabLayout(tab, edit=True, tabLabel=(
            (tab1, 'Model'),
            (tab2, 'Rig'),
            (tab3, 'Previs'),
            (tab4, 'Layout'),
            (tab5, 'Animation'),
            (tab6, 'Simulation'),
            (tab7, 'Effects'),
            (tab8, 'Lighting'),
            (tab9, 'Rendering')
        ))

        mc.formLayout(tab1, edit=True, attachForm=[
            (m_t1, 'top', 5), (m_t1, 'left', 10),
            (m_l1, 'top', 30), (m_l1, 'left', 10),
            (m_t2, 'top', 5), (m_t2, 'left', 140),
            (m_l2, 'top', 30), (m_l2, 'left', 140),
            (m_t3, 'top', 5), (m_t3, 'left', 270),
            (m_l3, 'top', 30), (m_l3, 'left', 270),
            (m_t4, 'top', 5), (m_t4, 'left', 400),
            (m_s1, 'top', 30), (m_s1, 'left', 400),
            (m_b1, 'top', 240), (m_b1, 'left', 10),
            (m_t5, 'top', 240), (m_t5, 'left', 100),
            (m_f1, 'top', 240), (m_f1, 'left', 170),
            (m_b2, 'top', 240), (m_b2, 'left', 700),
            (m_sp, 'top', 270), (m_sp, 'left', 10),
            (m_t6, 'top', 275), (m_t6, 'left', 10),
            (m_o1, 'top', 300), (m_o1, 'left', 10),
            (m_t7, 'top', 275), (m_t7, 'left', 140),
            (m_o2, 'top', 300), (m_o2, 'left', 140),
            (m_t8, 'top', 275), (m_t8, 'left', 270),
            (m_o3, 'top', 300), (m_o3, 'left', 270),
            (m_b3, 'top', 335), (m_b3, 'left', 10),
            (m_t9, 'top', 275), (m_t9, 'left', 400),
            (m_s2, 'top', 300), (m_s2, 'left', 400),
        ])

        mc.formLayout(tab3, edit=True, attachForm=[
            (pr_t1, 'top', 10), (pr_t1, 'left', 10),
            (pr_o1, 'top', 10), (pr_o1, 'left', 80),
            (pr_t2, 'top', 10), (pr_t2, 'left', 200),
            (pr_o2, 'top', 10), (pr_o2, 'left', 270),
            (pr_t3, 'top', 40), (pr_t3, 'left', 10),
            (pr_l1, 'top', 65), (pr_l1, 'left', 10),
            (pr_t4, 'top', 40), (pr_t4, 'left', 140),
            (pr_l2, 'top', 65), (pr_l2, 'left', 140),
            (pr_t5, 'top', 40), (pr_t5, 'left', 270),
            (pr_l3, 'top', 65), (pr_l3, 'left', 270),
            (pr_t6, 'top', 40), (pr_t6, 'left', 400),
            (pr_s1, 'top', 65), (pr_s1, 'left', 400),
            (pr_b1, 'top', 275), (pr_b1, 'left', 10),
            (pr_t7, 'top', 275), (pr_t7, 'left', 100),
            (pr_f1, 'top', 275), (pr_f1, 'left', 170),
            (pr_b2, 'top', 275), (pr_b2, 'left', 700),
            (pr_sp, 'top', 305), (pr_sp, 'left', 10),
            (pr_t8, 'top', 310), (pr_t8, 'left', 10),
            (pr_o3, 'top', 335), (pr_o3, 'left', 10),
            (pr_t9, 'top', 310), (pr_t9, 'left', 140),
            (pr_o4, 'top', 335), (pr_o4, 'left', 140),
            (pr_t10, 'top', 310), (pr_t10, 'left', 270),
            (pr_o5, 'top', 335), (pr_o5, 'left', 270),
            (pr_t11, 'top', 370), (pr_t11, 'left', 10),
            (pr_s2, 'top', 370), (pr_s2, 'left', 55),
            (pr_b3, 'top', 425), (pr_b3, 'left', 10),
            (pr_t12, 'top', 310), (pr_t12, 'left', 400),
            (pr_o6, 'top', 335), (pr_o6, 'left', 400),
            (pr_t13, 'top', 310), (pr_t13, 'left', 530),
            (pr_o7, 'top', 335), (pr_o7, 'left', 530),
            (pr_t14, 'top', 310), (pr_t14, 'left', 660),
            (pr_o8, 'top', 335), (pr_o8, 'left', 660),
            (pr_t15, 'top', 370), (pr_t15, 'left', 400),
            (pr_s3, 'top', 370), (pr_s3, 'left', 445),
            (pr_b4, 'top', 425), (pr_b4, 'left', 400),
        ])

        mc.showWindow(win)


a = NPipe()
a.getAsset()
a.ui()