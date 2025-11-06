from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Grab the number from the form using request.form()
        number = request.form.get("number")

        # Converts number to an int
        number = int(number)

        # Uses % to check if the number is odd or even
        result = "EVEN" if number % 2 == 0 else "ODD"

        # Passes both number and result to result.html
        return render_template('RESULTS.html', result=result, number=number)
    else:
        return render_template('GET.html')

if __name__ == '__main__':
    app.run(debug=True)



