from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import os
import trial1 as m
import log as l


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'F:/PROJECTS/Team Project/Main/Requests'

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    reqs = list(l.getLog()['pending'].keys())
    return render_template('home.html', reqs=reqs)
    

# @app.route('/dashboard', methods=['POST', 'GET'])
# def dashboard():
#     print(url_for('dashboard'))
#     print(request.method)
#     if request.method == 'POST':
#         if True:
#             reqs = list(l.getLog()['pending'].keys())
#             return render_template('home.html', reqs=reqs)
#         return redirect(url_for('login'))
#     else:
#         return redirect('login')


@app.route('/dashboard/createRequest', methods=['GET', 'POST'])
def createRequest():
    if request.method == 'POST':
        # print(dict(request.form))
        l.createReq(dict(request.form))
        f = request.files['file']
        if f.filename:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return redirect(url_for('dashboard'))
    else:
        return render_template('createReq.html')


@app.route('/dashboard/<id>')
def requesUI(id):
    return render_template('requestUI.html', data =[id, l.parseReqLog(id)])


@app.route('/dashboard/<id>/fetch')
def fetch(id):
    l.mailWalk(id)
    return render_template('requestUI.html', data =[id, l.parseReqLog(id)])


@app.route('/dashboard/<id>/delete')
def deleteReq(id):
    l.deleteReq(id)
    return redirect(url_for('dashboard'))


@app.route('/dashboard/<id>/edit', methods=['GET', 'POST'])
def editReq(id):
    if request.method == 'POST':
        l.createReq(dict(request.form))
        f = request.files['file']
        if f.filename:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return redirect(url_for('dashboard'))
    else:
        d = l.parseReqLog(id)
        return render_template('editReq.html', d = [id,d])

if __name__ == '__main__':
    app.run(debug=True)