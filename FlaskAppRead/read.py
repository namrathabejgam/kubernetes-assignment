from flask import Flask, render_template, request
import os.path
app = Flask(__name__)
@app.route('/')
def display():
  #Open the file back and read the contents
   if os.path.isfile("/folder/myfile.txt")==False:
      return "File doesn't exist!"
   f=open("/folder/myfile.txt", "r")
   if f.mode == 'r':
       contents =f.read()
   return render_template("main.html",contents = contents)
if __name__ == '__main__':
   app.run(host="0.0.0.0",port=5005,debug = True)
