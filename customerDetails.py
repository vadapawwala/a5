from flask import Flask, render_template, request

app = Flask(__name__)

customer_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global customer_list
    if request.method == 'POST':
        cust_name = request.form['CustName']
        email = request.form['email']
        mob_no = request.form['MobNo']
        address = request.form['address']
        pincode = request.form['pincode']

        # Store customer details in a dictionary
        customer_details = {
            'CustName': cust_name,
            'Email': email,
            'MobNo': mob_no,
            'Address': address,
            'Pincode': pincode
        }
        customer_list.append(customer_details)

    return render_template('customer.html', customer_list=customer_list)

if __name__ == '__main__':
    app.run(port=5009)