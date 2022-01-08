from tkinter import *
from tkinter import ttk
import asyncio



import settings
from deej import main as dj

class DJPY:

   def __init__(self,root):
      self.slider1=None
      self.slider2=None
      #title of window
      root.title("PY Deej")
      root.iconbitmap("assets/logo.ico")
      root.minsize(300, 200)

      mainframe = ttk.Frame(root, padding="3 3 12 12")
      mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
      # columnconfigure/rowconfigure tell the frame 
      # to expand to fill any space if the window is resized.
      root.columnconfigure(0, weight=1)
      root.rowconfigure(0, weight=1)


      # label that we'll manually update via the scale's command callback
      self.manual = ttk.Label(root)
      self.manual.grid(column=0, row=0, sticky='we')



      # Creates sliders
      #slider one
      self.slider1 = ttk.Scale(root, orient='vertical', length=150, from_=100.0, to=0.0, value=settings.slider1_value, command=self.update_lbl)
      self.slider1.set(100)
      self.slider1.grid(column=0, row=2, sticky='we')
      #slider two
      self.slider2 = ttk.Scale(root, orient='vertical', length=150, from_=100.0, to=0.0, value=settings.slider2_value, command=self.update_lbl)
      self.slider2.set(100)
      self.slider2.grid(column=1, row=2, sticky='we')

   def slider_getSTR(self):
      sliderValues = [
         "\n    -Slider 1 = "+str("{:.0f}".format(self.slider1.get()))
         #"\n    -Slider 2 = "+str("{:.0f}".format(self.slider2.get()))
         ]
      #Gets rid of quotes & brackets
      sliderValues = ', '.join(str(x) for x in sliderValues)
      #returns raw string.
      return sliderValues

   # The label from before that's updated to reflect the scale's value
   def update_lbl(self,val):
      self.manual['text'] = "Scale at:"+str(self.slider_getSTR())

   

async def main():
   async def make_window():
      root = Tk()
      DJPY(root)
      root.mainloop()
   
   CREATE_WINDOW = asyncio.create_task(make_window())
   CREATE_DJ = asyncio.create_task(dj())

   await CREATE_WINDOW
   await CREATE_DJ

asyncio.run(main())