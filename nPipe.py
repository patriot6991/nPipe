import maya.cmds as mc


class NPipe(object):
    def __init__(self):
        hoge = ''

    def ui(self, *args):
        win = mc.window('win', t='nPipe', w=815, h=420)

        menuBarLayout = mc.menuBarLayout()
        mc.menu(label='File')
        mc.menuItem(label='Setting')

        mc.menu(label='Help', helpMenu=True)
        mc.menuItem(label='About...')

        tab = mc.tabLayout(imw=5, imh=5, w=815, h=420)

        # -----------------------------------------------------------
        tab1 = mc.formLayout()
        m_t1 = mc.text(l=' Asset Name:', al='left', w=200, h=20)
        m_l1 = mc.textScrollList(w=120, h=200)
        m_t2 = mc.text(l=' LoD:', al='left', w=200, h=20)
        m_l2 = mc.textScrollList(w=120, h=200)
        m_t3 = mc.text(l=' Version:', al='left', w=200, h=20)
        m_l3 = mc.textScrollList(w=120, h=200)
        m_t4 = mc.text(l=' Note:', al='left', w=200, h=20)
        m_s1 = mc.scrollField(text='hoge', w=400, h=200)
        m_b1 = mc.button(l='import', w=80, h=25)
        m_t5 = mc.text(l='Directory:', al='right', w=60, h=25)
        m_f1 = mc.textField(text='directory', w=540, h=25)
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
        m_s2 = mc.scrollField(text='hoge', w=400, h=85)

        mc.setParent('..')

        # -----------------------------------------------------------
        tab2 = mc.formLayout()
        mc.setParent('..')

        # -----------------------------------------------------------
        tab3 = mc.formLayout()
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
            (m_b2, 'top', 240), (m_b2, 'left', 720),
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

        mc.showWindow(win)

a = NPipe()
a.ui()