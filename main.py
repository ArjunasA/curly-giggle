from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('widgets.kv')

class AppLayout(Widget):
	pass
	
class CalculatorApp(MDApp):
	def build(self):
		return AppLayout()
		
if __name__ == '__main__':
	CalculatorApp().run()

