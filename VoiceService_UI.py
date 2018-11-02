from VoiceService import Speech_text
from search import query
import tkinter as tk
import os 

file_dir=os.path.dirname(__file__)#the file's current dir
image_path=os.path.join(file_dir,'ccu_logo.png')


class Application_UI():
	def __init__(self):
		#tk.Frame.__init__(self)
		window=tk.Tk()
		window.title('VoiceService')
		window.geometry('480x270')
		#self.tk.grid()
		self.canvas = tk.Canvas(window,width=400,height=100)
		image_file = tk.PhotoImage(file=image_path)
		self.canvas.create_image(0,0, anchor='nw', image=image_file)
		self.canvas.pack(side='top')
		self.create_widgets(window)
		window.mainloop()

	def create_widgets(self,master):

		self.text_sp=tk.Text(master,width=55,height=5,font=('標楷',12))
		self.text_sp.place(x=240,y=160,anchor='center') # writing in same line would contribute AttributeError

		self.btn_record =tk.Button(master, text='Record',width=15, height=2,font=('times',11),command=lambda:self.text_sp.insert('end',Speech_text()))
		self.btn_record.place(x=160, y= 240,anchor='center')

		self.btn_confirm =tk.Button(master,text='Confirm',width=15, height=2,font=('times',11),command=lambda:query(self.text_sp.get(0.0,'end')))
		self.btn_confirm.place(x=320, y= 240,anchor='center')


if __name__ == '__main__':
	Application_UI()


