from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route('/')

def home():

    return render_template('dashboard.html')
 
@app.route('/new-claim')

def new_claim():

    return render_template('claim_form.html')
 
@app.route('/submit', methods=['POST'])

def submit():

    policy = request.form.get('policy')

    claim_type = request.form.get('claim_type')

    amount = request.form.get('amount')

    description = request.form.get('description')
 
    msg = f"""

    ✅ Claim Submitted Successfully! <br><br>

    Policy: {policy} <br>

    Type: {claim_type} <br>

    Amount: ₹{amount} <br>

    Description: {description} <br>

    """

    return msg
 
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

 