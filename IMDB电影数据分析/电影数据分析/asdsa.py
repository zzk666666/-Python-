from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    list1=[1,0,0,1]
    return render_template('show_data.html', list1)

if __name__ == '__main__':
    app.run(debug=True)