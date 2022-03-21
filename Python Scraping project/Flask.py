from pstats import Stats
from flask import Flask, redirect, send_file , url_for ,render_template , request
from script import Scrapper
from Stats import create_dash_application
import pandas as pd
import plotly.express as px
app = Flask(__name__)
create_dash_application(app,id=55742508)


@app.route('/') # home here we type in url
def Home():
   return render_template('Home.html', error="")
   # enter bar  redirect(url_for("url", url="data"))


@app.route('/Error') 
def Error():
   return render_template('Error.html')

@app.route('/result',methods = ['POST', 'GET'])
def Result():
   if request.method == 'POST':
      result = request.form
      scrap = Scrapper(result['Id'])
      id = result['Id']
      if scrap.error_test() == True:
         return render_template("Home.html" , error = "Valid ID")
      result = scrap.scraping_data()
      return render_template("Result.html",result = result , json = scrap.data_json() ,csv=scrap.data_csv() ,stats = f'/charts/{id}')

@app.route('/<file>')
def downloadFile(file):
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = f'{file}'
    return send_file(path, as_attachment=True)

@app.route("/charts/<int:id>")
def plots(id):
   df = pd.read_json (f"json_data{id}.json")
   sum = []
   for i in df['Treść wiadomości']:
       sum.append(len(i))
   
   avg = df['Ocena'].sum() / len(df['Ocena'])
   avg = "{:.1f}".format(avg)
   up = df['Przydatna opinia'].sum()
   down = df['Nieprzydatna opinia'].sum()
   fig1 = px.bar(df, x=df['Ocena'], y=[df['Przydatna opinia'],df['Nieprzydatna opinia']], title="Rozkład przydatnych i nieprzydanych opinii na ocenach")
   fig2=px.pie(df, values=df['Ocena'], names=df['Ocena'],hole=.3, title= 'Rozkład Ocen')
   fig1.show()
   fig2.show()
   return redirect(url_for("Home"))

if __name__ == '__main__':
   app.run()

