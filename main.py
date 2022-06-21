from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('widgets.kv')

class AppLayout(Widget):
	def show(self):
		list = []
		list.append(self.ids.input.text.split(','))
		f = int(list[0][0])
		d = int(list[0][1])-int(list[0][0])
		f_d = f-d
		expression = "Algebraic expression:"+str(d)+"n+"+str(f_d)
		commondiff = "common difference:"+str(d)
		self.ids.text.text = expression+"\n"+commondiff
	
class CalculatorApp(MDApp):
	def build(self):
		return AppLayout()
		
if __name__ == '__main__':
	CalculatorApp().run()

