from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/',methods = ['POST'])
def result():
      result = request.form['Text']
      file1 = open("/folder/myfile.txt","a+")
      file1.write(result+"\n")
      file1.close()
      return ""
if __name__ == '__main__':
   app.run(host="0.0.0.0",port=5000,debug = True)
