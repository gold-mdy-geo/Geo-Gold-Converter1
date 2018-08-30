from flask import Flask, render_template, url_for, request, jsonify
import z2u
import u2z
import w2u
import u2w


myapp=Flask(__name__)

@myapp.route("/")
def main():
    return render_template("index.html")

@myapp.route("/convert", methods=["POST"])
def convert():
    myinput = request.form['myinput']
    myoutput = request.form['myoutput']
    source = request.form['source']

    if myinput == "Zawgyi" and myoutput == "Unicode":
        output = z2u.convert(source)
        return jsonify({'output': output})
    if myinput == "Zawgyi" and myoutput == "WinMyanmar":
        output = z2u.convert(source)
        output = u2w.convert(output)
        return jsonify({'output': output})
    if myinput == "Unicode" and myoutput == "Zawgyi":
        output = u2z.convert(source)
        return jsonify({'output': output})
    if myinput == "Unicode" and myoutput == "WinMyanmar":
        output = u2w.convert(source)
        return jsonify({'output': output})
    if myinput == "WinMyanmar" and myoutput == "Zawgyi":
        output = w2u.convert(source)
        output = u2z.convert(output)
        return jsonify({'output': output})
    if myinput == "WinMyanmar" and myoutput == "Unicode":
        output = w2u.convert(source)
        return jsonify({'output': output})

    return jsonify({'output': "Enter your text"})

@myapp.route("/home")
def home():
    return render_template("home.html")

@myapp.route("/zg2win")
def zg2win():
    return render_template("zg2win.html")

@myapp.route("/uni2zg")
def uni2zg():
    return render_template("uni2zg.html")

@myapp.route("/uni2win")
def uni2win():
    return render_template("uni2win.html")

@myapp.route("/win2zg")
def win2zg():
    return render_template("win2zg.html")

@myapp.route("/win2uni")
def win2uni():
    return render_template("win2uni.html")

@myapp.route("/partner")
def partner():
    return render_template("partner.html")

@myapp.route("/question_and_answer")
def question_and_answer():
    return render_template("question_and_answer.html")

@myapp.route("/resources")
def resources():
    return render_template("resources.html")

@myapp.route("/tools")
def tools():
    return render_template("tools.html")

@myapp.route("/work")
def work():
    return render_template("work.html")


if __name__=="__main__":
    myapp.run(debug=True)
