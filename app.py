from flask import *
from persistence import *

app = Flask(__name__)

@app.route('/Donor', methods=['GET', 'POST'])
def donor():
    if request.method == "POST":

        item = request.form['Item']
        expiry = request.form['Expiry']
        quantity = request.form['Quantity']
        req = request.form['Req']
        email = 'email3'


        donor = Donor(item, expiry, quantity, req, email)
        create_donor(donor)
        return redirect(url_for('donorlist'))
    return render_template('Donor.html')


@app.route('/DonorSubmit')
def donorlist():
    l = get_donors()
    return render_template('DonorSubmit.html', list=l)





#@app.route('/donorUpdated')
#def donorUpdated():
   # l = get_donors()
   # return render_template('donorUpdated.html', list=l)


# UPDATE FOR DELETION
@app.route('/<string:id>/update', methods=('GET', 'POST'))
def update(id):
    post = get_donor(id)

    if request.method == 'POST':
        item = request.form['Item']
        expiry = request.form['Expiry']
        quantity = request.form['Quantity']
        req = request.form['Req']
        email = 'email3'
        error = None

        if not item:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.item = item
            post.expiry = expiry
            post.quantity = quantity
            post.req = req
            post.email = email
            update_donor(post)
            return redirect(url_for('donor'))

    return render_template('donorUpdate.html', post=post)


@app.route('/<string:id>/delete', methods=('GET', 'POST'))
def delete(id):
    delete_donors(id)
    posts = get_donors()
    return render_template('DonorSubmit.html', posts=posts)




@app.route('/admindonor')
def admindonor():

    return render_template('admindonor.html')








@app.route('/userprofile', methods=['GET', 'POST'])
def userprofile():

    if request.method == "POST":
        name = request.form['name']
        email1 = request.form['email1']
        address = request.form['address']
        people = request.form['people']

        userprofile = user(name, email1, address, people)
        update_user(userprofile)
        return render_template('userprofile.html', user=userprofile)
    return render_template('userprofile.html', u=user)

#@app.route('/admindonor')
#def donorlist():
   # l = get_donors()
    #return render_template('admin.html', list=l)












if __name__ == '__main__':
    app.run(debug=True)
