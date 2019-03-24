import tkinter as tk
import joblib
import numpy as np    
impmodel=joblib.load("GDP_model.sav")
root=tk.Tk()
tk.Label(root,text='Predict GDP of India',font="Verdana 20 bold",bg="#0099e6").pack(fill='x')
v1=tk.StringVar()
v2=tk.StringVar()
tk.Label(root,text='Enter the year:',font="Verdana 10 bold",bg="#0099e6").pack(fill='x')
def getoutput():
    global v1
    str1=v1.get()
    num=int(str1)
    a=np.array([[num]])
    op=impmodel.predict(a)
    op=op[0]
    str2=str(op)
    v2.set(str2)
tk.Entry(root,textvariable=v1).pack(fill='x')
tk.Button(root,text="Predict",padx=20,command=getoutput,bg="AntiqueWhite3").pack(fill="x",pady=5)
tk.Label(root,textvariable=v2,font="Verdana 20 bold",bg="#0edde6").pack(fill='x')
root.mainloop()