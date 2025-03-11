from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        architecture_value = request.form.get('architecture')
        client_name_value = request.form.get('client_name')
        value_2_4 = request.form.get('value_2_4')
        
        print(f"Architecture: {architecture_value}")
        print(f"Client Name: {client_name_value}")
        print(f"2.4: {value_2_4}")
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
