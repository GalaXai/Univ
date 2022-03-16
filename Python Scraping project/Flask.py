from flask import Flask, redirect, send_file , url_for ,render_template , request
from script import Scrapper
app = Flask(__name__)

@app.route('/') # home here we type in url
def Home():
   return render_template('Home.html')
   # enter bar  redirect(url_for("url", url="data"))


@app.route('/error')
def admin():
   return "Valid Url"

@app.route('/result',methods = ['POST', 'GET'])
def Result():
   if request.method == 'POST':
      result = request.form
      scrap = Scrapper(result['Id'])
      if scrap.error_test() == True:
         return redirect(url_for("Home", error = "Valid"))
      result = scrap.scraping_data()
      return render_template("Result.html",result = result , json = scrap.data_json())
      # return render_template("script.py",result = result)

@app.route('/<file>')
def downloadFile(file):
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = f'{file}'
    return send_file(path, as_attachment=True)
if __name__ == '__main__':
   app.run(debug = True)

