from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return '<button>Button in Sever</button>'

@app.route('/mypage')
def mypage():
   return 'This is My page'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)