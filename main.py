from flask import Flask, render_template
from flask import request, url_for, redirect, flash
from frankTest import hello_name
from flask_bootstrap import Bootstrap5
from chat import ai_get

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

'''
def ai_get(q):
    return "answer of (" + q + ")"
'''

@app.route("/home")
def home():
    return str(hello_name("Frank") + ". How dare you!")


@app.route("/hello/")
def hello():
    ID = "Hui Junxiong"
    Date = 1
    xxx.t()
    return render_template('hello.html',
                           ID=ID,
                           Date=Date)
@app.route("/")
def main():
    func_name = "main"
    return render_template('index.html',
                           Title = func_name)

@app.route('/form', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       return "Your name is "+ first_name + last_name
    return render_template("form.html")

@app.route('/ai', methods =["GET", "POST"])
def chatai():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       question = request.form.get("question")
       answer = ai_get(question)
       return render_template("chatai.html",
                              question=question,
                              answer = answer)
    return render_template("chatai.html")

@app.route("/test")
def test():
    func_name = "test"
    return render_template("test.html",
                           Title = func_name)


@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码

@app.errorhandler(500)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('500.html'), 500  # 返回模板和状态码


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
