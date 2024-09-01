import kivymd 
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
__version__ = "1.0"
#create a KivyMD class using MDApp
class App(MDApp):
    def build(self):
        sm = ScreenManager()
        a = Builder.load_file('main.kv')
        #sm.add_widget(Main_Screen(name = 'Main_screen'))
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.theme_primary_palette = 'Green'
        return a
        
    def back_screen(self):
        self.manager.current = ''
if __name__ == '__main__':
    App().run()