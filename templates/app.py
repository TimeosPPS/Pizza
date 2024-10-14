from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to our pizzeria!"

@app.route('/menu')
def menu():
    # Відкриття JSON файлу з меню
    with open('static/menu.json', 'r', encoding='utf-8') as f:
        pizzas = json.load(f)
    return render_template('menu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(port=5050, debug=True)

    #static for CCS and image
    #templates for html