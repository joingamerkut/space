from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        modme_id = request.form.get("modme_id")
        parol = request.form.get("parol")

        # Oddiy tekshiruv (demo uchun)
        if modme_id == "12345" and parol == "123456":
            return render_template('index.html')
    return render_template('login.html')
        


if __name__ == '__main__':
    app.run(debug=True)