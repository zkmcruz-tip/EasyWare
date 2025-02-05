from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.lang import Builder

from kivymd.theming import ThemeManager

Builder.load_string(
    '''
#:import toast kivymd.toast.toast


<MyRoot@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        title: "Test MDDropDownItem"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [['menu', lambda x: x]]

    FloatLayout:

        MDDropDownItem:
            id: dropdown_item
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            items: app.items
            dropdown_bg: [1, 1, 1, 1]

        MDRaisedButton:
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            text: 'Chek Item'
            on_release: toast(dropdown_item.current_item)
''')


class Test(MDApp):

    def build(self):
        self.items = [f"Item {i}" for i in range(50)]
        return Factory.MyRoot()


Test().run()