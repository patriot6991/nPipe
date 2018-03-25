import maya.cmds as mc
import urllib2
import json

class NPipe(object):
    def __init__(self):
        self.json = ''
        self.models = []
        self.model = ''
        self.LoDs = []
        self.versions = []
        self.note = ''

    def getModel(self, *args):
        f = open('C:/nPipe/model.json', 'r')
        self.json = json.load(f)
        self.models = self.json['model'].keys()

    def getLoD(self, model, *args):
        self.LoDs = []
        self.model = model
        self.LoDs = self.json['model'][model].keys()
        mc.textScrollList('m_l2', ra=True, append=self.LoDs, edit=True, enable=True)

    def getVersion(self, LoD, *args):
        self.versions = []
        self.versions = self.json['model'][self.model][LoD].keys()
        mc.textScrollList('m_l3', ra=True, append=self.versions, edit=True, enable=True)

    def selectNode(self, scrollList, *args):
        selectedNode = mc.textScrollList(scrollList, query=True, selectItem=True)
        if scrollList == 'm_l1':
            self.getLoD(selectedNode[0])
        else:
            self.getVersion(selectedNode[0])


    def ui(self, *args):
        if mc.window('main', ex=True) == True:
            mc.deleteUI('main', window=True)

        main = mc.window('main', t='nPipe')

        menuBarLayout = mc.menuBarLayout()
        mc.menu(label='File')
        mc.menuItem(label='Manager')
        mc.menuItem(label='Setting')

        mc.menu(label='Help', helpMenu=True)
        mc.menuItem(label='About...')

        tab = mc.tabLayout(imw=5, imh=5, w=795, h=505)

        # -----------------------------------------------------------
        tab1 = mc.formLayout()
        m_t1 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        m_l1 = mc.textScrollList('m_l1', w=120, h=200, append=self.models, selectCommand=lambda: self.selectNode('m_l1'))
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
        r_t1 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        r_l1 = mc.textScrollList('r_l1', w=120, h=200)
        r_t2 = mc.text(l=' Section:', al='left', w=200, h=20)
        r_l2 = mc.textScrollList('r_l2', w=120, h=200)
        r_t3 = mc.text(l=' Version:', al='left', w=200, h=20)
        r_l3 = mc.textScrollList('r_l3', w=120, h=200)
        r_t4 = mc.text(l=' Note:', al='left', w=200, h=20)
        r_s1 = mc.scrollField(text='hoge', w=380, h=200)
        r_b1 = mc.button(l='import', w=80, h=25)
        r_t5 = mc.text(l='Directory:', al='right', w=60, h=25)
        r_f1 = mc.textField(text='directory', w=520, h=25)
        r_b2 = mc.button(l='open', w=80, h=25)

        r_sp = mc.separator(w=790)

        r_t6 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        r_o1 = mc.optionMenu(w=120, h=25)
        r_t7 = mc.text(l=' Section:', al='left', w=200, h=20)
        r_o2 = mc.optionMenu(w=120, h=25)
        r_t8 = mc.text(l=' Status:', al='left', w=200, h=20)
        r_o3 = mc.optionMenu(w=120, h=25)
        r_b3 = mc.button(l='Publish!!', w=380, h=50)
        r_t9 = mc.text(l=' Note:', al='left', w=200, h=20)
        r_s2 = mc.scrollField(text='hoge', w=380, h=85)

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
        pr_b4 = mc.button(l='Publish Movie!!', w=380, h=50)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab4 = mc.formLayout()
        la_o1 = mc.optionMenu(w=120, h=25)
        la_t1 = mc.text(l=' Shot:', al='right', w=60, h=20)
        la_o2 = mc.optionMenu(w=120, h=25)
        la_t2 = mc.text(l=' Cut:', al='right', w=60, h=20)
        la_t3 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        la_l1 = mc.textScrollList(w=120, h=200)
        la_t4 = mc.text(l=' LoD:', al='left', w=200, h=20)
        la_l2 = mc.textScrollList(w=120, h=200)
        la_t5 = mc.text(l=' Version:', al='left', w=200, h=20)
        la_l3 = mc.textScrollList(w=120, h=200)
        la_t6 = mc.text(l=' Note:', al='left', w=200, h=20)
        la_s1 = mc.scrollField(text='hoge', w=380, h=200)
        la_b1 = mc.button(l='import', w=80, h=25)
        la_t7 = mc.text(l='Directory:', al='right', w=60, h=25)
        la_f1 = mc.textField(text='directory', w=520, h=25)
        la_b2 = mc.button(l='open', w=80, h=25)

        la_sp = mc.separator(w=790)

        la_t8 = mc.text(l=' Shot:', al='left', w=200, h=20)
        la_o3 = mc.optionMenu(w=120, h=25)
        la_t9 = mc.text(l=' Cut:', al='left', w=200, h=20)
        la_o4 = mc.optionMenu(w=120, h=25)
        la_t10 = mc.text(l=' Status:', al='left', w=200, h=20)
        la_o5 = mc.optionMenu(w=120, h=25)
        la_t11 = mc.text(l=' Note:', al='left', w=200, h=20)
        la_s2 = mc.scrollField(text='hoge', w=335, h=45)
        la_b3 = mc.button(l='Publish Camera!!', w=380, h=50)

        la_t12 = mc.text(l=' Shot:', al='left', w=200, h=20)
        la_o6 = mc.optionMenu(w=120, h=25)
        la_t13 = mc.text(l=' Cut:', al='left', w=200, h=20)
        la_o7 = mc.optionMenu(w=120, h=25)
        la_t14 = mc.text(l=' Status:', al='left', w=200, h=20)
        la_o8 = mc.optionMenu(w=120, h=25)
        la_t15 = mc.text(l=' Note:', al='left', w=200, h=20)
        la_s3 = mc.scrollField(text='hoge', w=335, h=45)
        la_b4 = mc.button(l='Publish Image!!', w=380, h=50)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab5 = mc.formLayout()
        a_o1 = mc.optionMenu(w=120, h=25)
        a_t1 = mc.text(l=' Shot:', al='right', w=60, h=20)
        a_o2 = mc.optionMenu(w=120, h=25)
        a_t2 = mc.text(l=' Cut:', al='right', w=60, h=20)
        a_t3 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        a_l1 = mc.textScrollList(w=120, h=200)
        a_t4 = mc.text(l=' LoD:', al='left', w=200, h=20)
        a_l2 = mc.textScrollList(w=120, h=200)
        a_t5 = mc.text(l=' Version:', al='left', w=200, h=20)
        a_l3 = mc.textScrollList(w=120, h=200)
        a_t6 = mc.text(l=' Note:', al='left', w=200, h=20)
        a_s1 = mc.scrollField(text='hoge', w=380, h=200)
        a_b1 = mc.button(l='import', w=80, h=25)
        a_t7 = mc.text(l='Directory:', al='right', w=60, h=25)
        a_f1 = mc.textField(text='directory', w=520, h=25)
        a_b2 = mc.button(l='open', w=80, h=25)

        a_sp = mc.separator(w=790)

        a_t8 = mc.text(l=' Shot:', al='left', w=200, h=20)
        a_o3 = mc.optionMenu(w=120, h=25)
        a_t9 = mc.text(l=' Cut:', al='left', w=200, h=20)
        a_o4 = mc.optionMenu(w=120, h=25)
        a_t10 = mc.text(l=' Status:', al='left', w=200, h=20)
        a_o5 = mc.optionMenu(w=120, h=25)
        a_t11 = mc.text(l=' Note:', al='left', w=200, h=20)
        a_s2 = mc.scrollField(text='hoge', w=335, h=45)
        a_b3 = mc.button(l='Publish Camera!!', w=380, h=50)

        a_t12 = mc.text(l=' Shot:', al='left', w=200, h=20)
        a_o6 = mc.optionMenu(w=120, h=25)
        a_t13 = mc.text(l=' Cut:', al='left', w=200, h=20)
        a_o7 = mc.optionMenu(w=120, h=25)
        a_t14 = mc.text(l=' Status:', al='left', w=200, h=20)
        a_o8 = mc.optionMenu(w=120, h=25)
        a_t15 = mc.text(l=' Note:', al='left', w=200, h=20)
        a_s3 = mc.scrollField(text='hoge', w=335, h=45)
        a_b4 = mc.button(l='Publish Movie!!', w=380, h=50)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab6 = mc.formLayout()
        s_o1 = mc.optionMenu(w=120, h=25)
        s_t1 = mc.text(l=' Shot:', al='right', w=60, h=20)
        s_o2 = mc.optionMenu(w=120, h=25)
        s_t2 = mc.text(l=' Cut:', al='right', w=60, h=20)
        s_t3 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        s_l1 = mc.textScrollList(w=120, h=200)
        s_t4 = mc.text(l=' LoD:', al='left', w=200, h=20)
        s_l2 = mc.textScrollList(w=120, h=200)
        s_t5 = mc.text(l=' Version:', al='left', w=200, h=20)
        s_l3 = mc.textScrollList(w=120, h=200)
        s_t6 = mc.text(l=' Note:', al='left', w=200, h=20)
        s_s1 = mc.scrollField(text='hoge', w=380, h=200)
        s_b1 = mc.button(l='import', w=80, h=25)
        s_t7 = mc.text(l='Directory:', al='right', w=60, h=25)
        s_f1 = mc.textField(text='directory', w=520, h=25)
        s_b2 = mc.button(l='open', w=80, h=25)

        s_sp = mc.separator(w=790)

        s_t8 = mc.text(l=' Shot:', al='left', w=200, h=20)
        s_o3 = mc.optionMenu(w=120, h=25)
        s_t9 = mc.text(l=' Cut:', al='left', w=200, h=20)
        s_o4 = mc.optionMenu(w=120, h=25)
        s_t10 = mc.text(l=' Status:', al='left', w=200, h=20)
        s_o5 = mc.optionMenu(w=120, h=25)
        s_t11 = mc.text(l=' Note:', al='left', w=200, h=20)
        s_s2 = mc.scrollField(text='hoge', w=335, h=45)
        s_b3 = mc.button(l='Publish Scene!!', w=380, h=50)

        s_t12 = mc.text(l=' Shot:', al='left', w=200, h=20)
        s_o6 = mc.optionMenu(w=120, h=25)
        s_t13 = mc.text(l=' Cut:', al='left', w=200, h=20)
        s_o7 = mc.optionMenu(w=120, h=25)
        s_t14 = mc.text(l=' Status:', al='left', w=200, h=20)
        s_o8 = mc.optionMenu(w=120, h=25)
        s_t15 = mc.text(l=' Note:', al='left', w=200, h=20)
        s_s3 = mc.scrollField(text='hoge', w=335, h=45)
        s_b4 = mc.button(l='Publish Cache!!', w=380, h=50)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab7 = mc.formLayout()
        e_o1 = mc.optionMenu(w=120, h=25)
        e_t1 = mc.text(l=' Shot:', al='right', w=60, h=20)
        e_o2 = mc.optionMenu(w=120, h=25)
        e_t2 = mc.text(l=' Cut:', al='right', w=60, h=20)
        e_t3 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        e_l1 = mc.textScrollList(w=120, h=200)
        e_t4 = mc.text(l=' LoD:', al='left', w=200, h=20)
        e_l2 = mc.textScrollList(w=120, h=200)
        e_t5 = mc.text(l=' Version:', al='left', w=200, h=20)
        e_l3 = mc.textScrollList(w=120, h=200)
        e_t6 = mc.text(l=' Note:', al='left', w=200, h=20)
        e_s1 = mc.scrollField(text='hoge', w=380, h=200)
        e_b1 = mc.button(l='import', w=80, h=25)
        e_t7 = mc.text(l='Directory:', al='right', w=60, h=25)
        e_f1 = mc.textField(text='directory', w=520, h=25)
        e_b2 = mc.button(l='open', w=80, h=25)

        e_sp = mc.separator(w=790)

        e_t8 = mc.text(l=' Shot:', al='left', w=200, h=20)
        e_o3 = mc.optionMenu(w=120, h=25)
        e_t9 = mc.text(l=' Cut:', al='left', w=200, h=20)
        e_o4 = mc.optionMenu(w=120, h=25)
        e_t10 = mc.text(l=' Status:', al='left', w=200, h=20)
        e_o5 = mc.optionMenu(w=120, h=25)
        e_t11 = mc.text(l=' Note:', al='left', w=200, h=20)
        e_s2 = mc.scrollField(text='hoge', w=335, h=45)
        e_b3 = mc.button(l='Publish Scene!!', w=380, h=50)

        e_t12 = mc.text(l=' Shot:', al='left', w=200, h=20)
        e_o6 = mc.optionMenu(w=120, h=25)
        e_t13 = mc.text(l=' Cut:', al='left', w=200, h=20)
        e_o7 = mc.optionMenu(w=120, h=25)
        e_t14 = mc.text(l=' Status:', al='left', w=200, h=20)
        e_o8 = mc.optionMenu(w=120, h=25)
        e_t15 = mc.text(l=' Note:', al='left', w=200, h=20)
        e_s3 = mc.scrollField(text='hoge', w=335, h=45)
        e_b4 = mc.button(l='Publish Cache!!', w=380, h=50)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab8 = mc.formLayout()
        li_o1 = mc.optionMenu(w=120, h=25)
        li_t1 = mc.text(l=' Shot:', al='right', w=60, h=20)
        li_o2 = mc.optionMenu(w=120, h=25)
        li_t2 = mc.text(l=' Cut:', al='right', w=60, h=20)
        li_t3 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        li_l1 = mc.textScrollList(w=120, h=200)
        li_t4 = mc.text(l=' LoD:', al='left', w=200, h=20)
        li_l2 = mc.textScrollList(w=120, h=200)
        li_t5 = mc.text(l=' Version:', al='left', w=200, h=20)
        li_l3 = mc.textScrollList(w=120, h=200)
        li_t6 = mc.text(l=' Note:', al='left', w=200, h=20)
        li_s1 = mc.scrollField(text='hoge', w=380, h=200)
        li_b1 = mc.button(l='import', w=80, h=25)
        li_t7 = mc.text(l='Directory:', al='right', w=60, h=25)
        li_f1 = mc.textField(text='directory', w=520, h=25)
        li_b2 = mc.button(l='open', w=80, h=25)

        li_sp = mc.separator(w=790)

        li_t8 = mc.text(l=' Shot:', al='left', w=200, h=20)
        li_o3 = mc.optionMenu(w=120, h=25)
        li_t9 = mc.text(l=' Cut:', al='left', w=200, h=20)
        li_o4 = mc.optionMenu(w=120, h=25)
        li_t10 = mc.text(l=' Status:', al='left', w=200, h=20)
        li_o5 = mc.optionMenu(w=120, h=25)
        li_t11 = mc.text(l=' Note:', al='left', w=200, h=20)
        li_s2 = mc.scrollField(text='hoge', w=335, h=45)
        li_b3 = mc.button(l='Publish Scene!!', w=380, h=50)

        li_t12 = mc.text(l=' Shot:', al='left', w=200, h=20)
        li_o6 = mc.optionMenu(w=120, h=25)
        li_t13 = mc.text(l=' Cut:', al='left', w=200, h=20)
        li_o7 = mc.optionMenu(w=120, h=25)
        li_t14 = mc.text(l=' Status:', al='left', w=200, h=20)
        li_o8 = mc.optionMenu(w=120, h=25)
        li_t15 = mc.text(l=' Note:', al='left', w=200, h=20)
        li_s3 = mc.scrollField(text='hoge', w=335, h=45)
        li_b4 = mc.button(l='Publish Light!!', w=380, h=50)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab9 = mc.formLayout()
        re_o1 = mc.optionMenu(w=120, h=25)
        re_t1 = mc.text(l=' Shot:', al='right', w=60, h=20)
        re_o2 = mc.optionMenu(w=120, h=25)
        re_t2 = mc.text(l=' Cut:', al='right', w=60, h=20)
        re_t3 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        re_l1 = mc.textScrollList(w=120, h=200)
        re_t4 = mc.text(l=' LoD:', al='left', w=200, h=20)
        re_l2 = mc.textScrollList(w=120, h=200)
        re_t5 = mc.text(l=' Version:', al='left', w=200, h=20)
        re_l3 = mc.textScrollList(w=120, h=200)
        re_t6 = mc.text(l=' Note:', al='left', w=200, h=20)
        re_s1 = mc.scrollField(text='hoge', w=380, h=200)
        re_b1 = mc.button(l='import', w=80, h=25)
        re_t7 = mc.text(l='Directory:', al='right', w=60, h=25)
        re_f1 = mc.textField(text='directory', w=520, h=25)
        re_b2 = mc.button(l='open', w=80, h=25)

        re_sp = mc.separator(w=790)

        re_t8 = mc.text(l=' Shot:', al='left', w=200, h=20)
        re_o3 = mc.optionMenu(w=120, h=25)
        re_t9 = mc.text(l=' Cut:', al='left', w=200, h=20)
        re_o4 = mc.optionMenu(w=120, h=25)
        re_t10 = mc.text(l=' Status:', al='left', w=200, h=20)
        re_o5 = mc.optionMenu(w=120, h=25)
        re_t11 = mc.text(l=' Note:', al='left', w=200, h=20)
        re_s2 = mc.scrollField(text='hoge', w=335, h=45)
        re_b3 = mc.button(l='Publish Scene!!', w=380, h=50)

        re_t12 = mc.text(l=' Shot:', al='left', w=200, h=20)
        re_o6 = mc.optionMenu(w=120, h=25)
        re_t13 = mc.text(l=' Cut:', al='left', w=200, h=20)
        re_o7 = mc.optionMenu(w=120, h=25)
        re_t14 = mc.text(l=' Status:', al='left', w=200, h=20)
        re_o8 = mc.optionMenu(w=120, h=25)
        re_t15 = mc.text(l=' Note:', al='left', w=200, h=20)
        re_s3 = mc.scrollField(text='hoge', w=335, h=45)
        re_b4 = mc.button(l='Send Render Job!!', w=380, h=50)

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

        mc.formLayout(tab2, edit=True, attachForm=[
            (r_t1, 'top', 5), (r_t1, 'left', 10),
            (r_l1, 'top', 30), (r_l1, 'left', 10),
            (r_t2, 'top', 5), (r_t2, 'left', 140),
            (r_l2, 'top', 30), (r_l2, 'left', 140),
            (r_t3, 'top', 5), (r_t3, 'left', 270),
            (r_l3, 'top', 30), (r_l3, 'left', 270),
            (r_t4, 'top', 5), (r_t4, 'left', 400),
            (r_s1, 'top', 30), (r_s1, 'left', 400),
            (r_b1, 'top', 240), (r_b1, 'left', 10),
            (r_t5, 'top', 240), (r_t5, 'left', 100),
            (r_f1, 'top', 240), (r_f1, 'left', 170),
            (r_b2, 'top', 240), (r_b2, 'left', 700),
            (r_sp, 'top', 270), (r_sp, 'left', 10),
            (r_t6, 'top', 275), (r_t6, 'left', 10),
            (r_o1, 'top', 300), (r_o1, 'left', 10),
            (r_t7, 'top', 275), (r_t7, 'left', 140),
            (r_o2, 'top', 300), (r_o2, 'left', 140),
            (r_t8, 'top', 275), (r_t8, 'left', 270),
            (r_o3, 'top', 300), (r_o3, 'left', 270),
            (r_b3, 'top', 335), (r_b3, 'left', 10),
            (r_t9, 'top', 275), (r_t9, 'left', 400),
            (r_s2, 'top', 300), (r_s2, 'left', 400),
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

        mc.formLayout(tab4, edit=True, attachForm=[
            (la_t1, 'top', 10), (la_t1, 'left', 10),
            (la_o1, 'top', 10), (la_o1, 'left', 80),
            (la_t2, 'top', 10), (la_t2, 'left', 200),
            (la_o2, 'top', 10), (la_o2, 'left', 270),
            (la_t3, 'top', 40), (la_t3, 'left', 10),
            (la_l1, 'top', 65), (la_l1, 'left', 10),
            (la_t4, 'top', 40), (la_t4, 'left', 140),
            (la_l2, 'top', 65), (la_l2, 'left', 140),
            (la_t5, 'top', 40), (la_t5, 'left', 270),
            (la_l3, 'top', 65), (la_l3, 'left', 270),
            (la_t6, 'top', 40), (la_t6, 'left', 400),
            (la_s1, 'top', 65), (la_s1, 'left', 400),
            (la_b1, 'top', 275), (la_b1, 'left', 10),
            (la_t7, 'top', 275), (la_t7, 'left', 100),
            (la_f1, 'top', 275), (la_f1, 'left', 170),
            (la_b2, 'top', 275), (la_b2, 'left', 700),
            (la_sp, 'top', 305), (la_sp, 'left', 10),
            (la_t8, 'top', 310), (la_t8, 'left', 10),
            (la_o3, 'top', 335), (la_o3, 'left', 10),
            (la_t9, 'top', 310), (la_t9, 'left', 140),
            (la_o4, 'top', 335), (la_o4, 'left', 140),
            (la_t10, 'top', 310), (la_t10, 'left', 270),
            (la_o5, 'top', 335), (la_o5, 'left', 270),
            (la_t11, 'top', 370), (la_t11, 'left', 10),
            (la_s2, 'top', 370), (la_s2, 'left', 55),
            (la_b3, 'top', 425), (la_b3, 'left', 10),
            (la_t12, 'top', 310), (la_t12, 'left', 400),
            (la_o6, 'top', 335), (la_o6, 'left', 400),
            (la_t13, 'top', 310), (la_t13, 'left', 530),
            (la_o7, 'top', 335), (la_o7, 'left', 530),
            (la_t14, 'top', 310), (la_t14, 'left', 660),
            (la_o8, 'top', 335), (la_o8, 'left', 660),
            (la_t15, 'top', 370), (la_t15, 'left', 400),
            (la_s3, 'top', 370), (la_s3, 'left', 445),
            (la_b4, 'top', 425), (la_b4, 'left', 400),
        ])

        mc.formLayout(tab5, edit=True, attachForm=[
            (a_t1, 'top', 10), (a_t1, 'left', 10),
            (a_o1, 'top', 10), (a_o1, 'left', 80),
            (a_t2, 'top', 10), (a_t2, 'left', 200),
            (a_o2, 'top', 10), (a_o2, 'left', 270),
            (a_t3, 'top', 40), (a_t3, 'left', 10),
            (a_l1, 'top', 65), (a_l1, 'left', 10),
            (a_t4, 'top', 40), (a_t4, 'left', 140),
            (a_l2, 'top', 65), (a_l2, 'left', 140),
            (a_t5, 'top', 40), (a_t5, 'left', 270),
            (a_l3, 'top', 65), (a_l3, 'left', 270),
            (a_t6, 'top', 40), (a_t6, 'left', 400),
            (a_s1, 'top', 65), (a_s1, 'left', 400),
            (a_b1, 'top', 275), (a_b1, 'left', 10),
            (a_t7, 'top', 275), (a_t7, 'left', 100),
            (a_f1, 'top', 275), (a_f1, 'left', 170),
            (a_b2, 'top', 275), (a_b2, 'left', 700),
            (a_sp, 'top', 305), (a_sp, 'left', 10),
            (a_t8, 'top', 310), (a_t8, 'left', 10),
            (a_o3, 'top', 335), (a_o3, 'left', 10),
            (a_t9, 'top', 310), (a_t9, 'left', 140),
            (a_o4, 'top', 335), (a_o4, 'left', 140),
            (a_t10, 'top', 310), (a_t10, 'left', 270),
            (a_o5, 'top', 335), (a_o5, 'left', 270),
            (a_t11, 'top', 370), (a_t11, 'left', 10),
            (a_s2, 'top', 370), (a_s2, 'left', 55),
            (a_b3, 'top', 425), (a_b3, 'left', 10),
            (a_t12, 'top', 310), (a_t12, 'left', 400),
            (a_o6, 'top', 335), (a_o6, 'left', 400),
            (a_t13, 'top', 310), (a_t13, 'left', 530),
            (a_o7, 'top', 335), (a_o7, 'left', 530),
            (a_t14, 'top', 310), (a_t14, 'left', 660),
            (a_o8, 'top', 335), (a_o8, 'left', 660),
            (a_t15, 'top', 370), (a_t15, 'left', 400),
            (a_s3, 'top', 370), (a_s3, 'left', 445),
            (a_b4, 'top', 425), (a_b4, 'left', 400),
        ])

        mc.formLayout(tab6, edit=True, attachForm=[
            (s_t1, 'top', 10), (s_t1, 'left', 10),
            (s_o1, 'top', 10), (s_o1, 'left', 80),
            (s_t2, 'top', 10), (s_t2, 'left', 200),
            (s_o2, 'top', 10), (s_o2, 'left', 270),
            (s_t3, 'top', 40), (s_t3, 'left', 10),
            (s_l1, 'top', 65), (s_l1, 'left', 10),
            (s_t4, 'top', 40), (s_t4, 'left', 140),
            (s_l2, 'top', 65), (s_l2, 'left', 140),
            (s_t5, 'top', 40), (s_t5, 'left', 270),
            (s_l3, 'top', 65), (s_l3, 'left', 270),
            (s_t6, 'top', 40), (s_t6, 'left', 400),
            (s_s1, 'top', 65), (s_s1, 'left', 400),
            (s_b1, 'top', 275), (s_b1, 'left', 10),
            (s_t7, 'top', 275), (s_t7, 'left', 100),
            (s_f1, 'top', 275), (s_f1, 'left', 170),
            (s_b2, 'top', 275), (s_b2, 'left', 700),
            (s_sp, 'top', 305), (s_sp, 'left', 10),
            (s_t8, 'top', 310), (s_t8, 'left', 10),
            (s_o3, 'top', 335), (s_o3, 'left', 10),
            (s_t9, 'top', 310), (s_t9, 'left', 140),
            (s_o4, 'top', 335), (s_o4, 'left', 140),
            (s_t10, 'top', 310), (s_t10, 'left', 270),
            (s_o5, 'top', 335), (s_o5, 'left', 270),
            (s_t11, 'top', 370), (s_t11, 'left', 10),
            (s_s2, 'top', 370), (s_s2, 'left', 55),
            (s_b3, 'top', 425), (s_b3, 'left', 10),
            (s_t12, 'top', 310), (s_t12, 'left', 400),
            (s_o6, 'top', 335), (s_o6, 'left', 400),
            (s_t13, 'top', 310), (s_t13, 'left', 530),
            (s_o7, 'top', 335), (s_o7, 'left', 530),
            (s_t14, 'top', 310), (s_t14, 'left', 660),
            (s_o8, 'top', 335), (s_o8, 'left', 660),
            (s_t15, 'top', 370), (s_t15, 'left', 400),
            (s_s3, 'top', 370), (s_s3, 'left', 445),
            (s_b4, 'top', 425), (s_b4, 'left', 400),
        ])

        mc.formLayout(tab7, edit=True, attachForm=[
            (e_t1, 'top', 10), (e_t1, 'left', 10),
            (e_o1, 'top', 10), (e_o1, 'left', 80),
            (e_t2, 'top', 10), (e_t2, 'left', 200),
            (e_o2, 'top', 10), (e_o2, 'left', 270),
            (e_t3, 'top', 40), (e_t3, 'left', 10),
            (e_l1, 'top', 65), (e_l1, 'left', 10),
            (e_t4, 'top', 40), (e_t4, 'left', 140),
            (e_l2, 'top', 65), (e_l2, 'left', 140),
            (e_t5, 'top', 40), (e_t5, 'left', 270),
            (e_l3, 'top', 65), (e_l3, 'left', 270),
            (e_t6, 'top', 40), (e_t6, 'left', 400),
            (e_s1, 'top', 65), (e_s1, 'left', 400),
            (e_b1, 'top', 275), (e_b1, 'left', 10),
            (e_t7, 'top', 275), (e_t7, 'left', 100),
            (e_f1, 'top', 275), (e_f1, 'left', 170),
            (e_b2, 'top', 275), (e_b2, 'left', 700),
            (e_sp, 'top', 305), (e_sp, 'left', 10),
            (e_t8, 'top', 310), (e_t8, 'left', 10),
            (e_o3, 'top', 335), (e_o3, 'left', 10),
            (e_t9, 'top', 310), (e_t9, 'left', 140),
            (e_o4, 'top', 335), (e_o4, 'left', 140),
            (e_t10, 'top', 310), (e_t10, 'left', 270),
            (e_o5, 'top', 335), (e_o5, 'left', 270),
            (e_t11, 'top', 370), (e_t11, 'left', 10),
            (e_s2, 'top', 370), (e_s2, 'left', 55),
            (e_b3, 'top', 425), (e_b3, 'left', 10),
            (e_t12, 'top', 310), (e_t12, 'left', 400),
            (e_o6, 'top', 335), (e_o6, 'left', 400),
            (e_t13, 'top', 310), (e_t13, 'left', 530),
            (e_o7, 'top', 335), (e_o7, 'left', 530),
            (e_t14, 'top', 310), (e_t14, 'left', 660),
            (e_o8, 'top', 335), (e_o8, 'left', 660),
            (e_t15, 'top', 370), (e_t15, 'left', 400),
            (e_s3, 'top', 370), (e_s3, 'left', 445),
            (e_b4, 'top', 425), (e_b4, 'left', 400),
        ])

        mc.formLayout(tab8, edit=True, attachForm=[
            (li_t1, 'top', 10), (li_t1, 'left', 10),
            (li_o1, 'top', 10), (li_o1, 'left', 80),
            (li_t2, 'top', 10), (li_t2, 'left', 200),
            (li_o2, 'top', 10), (li_o2, 'left', 270),
            (li_t3, 'top', 40), (li_t3, 'left', 10),
            (li_l1, 'top', 65), (li_l1, 'left', 10),
            (li_t4, 'top', 40), (li_t4, 'left', 140),
            (li_l2, 'top', 65), (li_l2, 'left', 140),
            (li_t5, 'top', 40), (li_t5, 'left', 270),
            (li_l3, 'top', 65), (li_l3, 'left', 270),
            (li_t6, 'top', 40), (li_t6, 'left', 400),
            (li_s1, 'top', 65), (li_s1, 'left', 400),
            (li_b1, 'top', 275), (li_b1, 'left', 10),
            (li_t7, 'top', 275), (li_t7, 'left', 100),
            (li_f1, 'top', 275), (li_f1, 'left', 170),
            (li_b2, 'top', 275), (li_b2, 'left', 700),
            (li_sp, 'top', 305), (li_sp, 'left', 10),
            (li_t8, 'top', 310), (li_t8, 'left', 10),
            (li_o3, 'top', 335), (li_o3, 'left', 10),
            (li_t9, 'top', 310), (li_t9, 'left', 140),
            (li_o4, 'top', 335), (li_o4, 'left', 140),
            (li_t10, 'top', 310), (li_t10, 'left', 270),
            (li_o5, 'top', 335), (li_o5, 'left', 270),
            (li_t11, 'top', 370), (li_t11, 'left', 10),
            (li_s2, 'top', 370), (li_s2, 'left', 55),
            (li_b3, 'top', 425), (li_b3, 'left', 10),
            (li_t12, 'top', 310), (li_t12, 'left', 400),
            (li_o6, 'top', 335), (li_o6, 'left', 400),
            (li_t13, 'top', 310), (li_t13, 'left', 530),
            (li_o7, 'top', 335), (li_o7, 'left', 530),
            (li_t14, 'top', 310), (li_t14, 'left', 660),
            (li_o8, 'top', 335), (li_o8, 'left', 660),
            (li_t15, 'top', 370), (li_t15, 'left', 400),
            (li_s3, 'top', 370), (li_s3, 'left', 445),
            (li_b4, 'top', 425), (li_b4, 'left', 400),
        ])

        mc.formLayout(tab9, edit=True, attachForm=[
            (re_t1, 'top', 10), (re_t1, 'left', 10),
            (re_o1, 'top', 10), (re_o1, 'left', 80),
            (re_t2, 'top', 10), (re_t2, 'left', 200),
            (re_o2, 'top', 10), (re_o2, 'left', 270),
            (re_t3, 'top', 40), (re_t3, 'left', 10),
            (re_l1, 'top', 65), (re_l1, 'left', 10),
            (re_t4, 'top', 40), (re_t4, 'left', 140),
            (re_l2, 'top', 65), (re_l2, 'left', 140),
            (re_t5, 'top', 40), (re_t5, 'left', 270),
            (re_l3, 'top', 65), (re_l3, 'left', 270),
            (re_t6, 'top', 40), (re_t6, 'left', 400),
            (re_s1, 'top', 65), (re_s1, 'left', 400),
            (re_b1, 'top', 275), (re_b1, 'left', 10),
            (re_t7, 'top', 275), (re_t7, 'left', 100),
            (re_f1, 'top', 275), (re_f1, 'left', 170),
            (re_b2, 'top', 275), (re_b2, 'left', 700),
            (re_sp, 'top', 305), (re_sp, 'left', 10),
            (re_t8, 'top', 310), (re_t8, 'left', 10),
            (re_o3, 'top', 335), (re_o3, 'left', 10),
            (re_t9, 'top', 310), (re_t9, 'left', 140),
            (re_o4, 'top', 335), (re_o4, 'left', 140),
            (re_t10, 'top', 310), (re_t10, 'left', 270),
            (re_o5, 'top', 335), (re_o5, 'left', 270),
            (re_t11, 'top', 370), (re_t11, 'left', 10),
            (re_s2, 'top', 370), (re_s2, 'left', 55),
            (re_b3, 'top', 425), (re_b3, 'left', 10),
            (re_t12, 'top', 310), (re_t12, 'left', 400),
            (re_o6, 'top', 335), (re_o6, 'left', 400),
            (re_t13, 'top', 310), (re_t13, 'left', 530),
            (re_o7, 'top', 335), (re_o7, 'left', 530),
            (re_t14, 'top', 310), (re_t14, 'left', 660),
            (re_o8, 'top', 335), (re_o8, 'left', 660),
            (re_t15, 'top', 370), (re_t15, 'left', 400),
            (re_s3, 'top', 370), (re_s3, 'left', 445),
            (re_b4, 'top', 425), (re_b4, 'left', 400),
        ])

        mc.showWindow(main)


a = NPipe()
a.getModel()
a.ui()