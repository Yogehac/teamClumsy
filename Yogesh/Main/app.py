from flask import Flask, render_template, request, url_for, redirect, send_file, jsonify
from flask_cors import CORS

from werkzeug.utils import secure_filename
import os
import trial1 as m
import log as l
import paths as pp
import makeReport as mk


app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = pp.requestDir

isAuthorized = m.login()


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        f = request.form
        if m.login(f['email'], f['pword']):
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', d=True)
    return render_template('login.html', d=False)


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    if isAuthorized:
        reqs = list(l.getLog()['pending'].keys())
        return render_template('home.html', reqs=reqs)
    return redirect(url_for('login'))


@app.route('/dashboard/createRequest', methods=['GET', 'POST'])
def createRequest():
    if request.method == 'POST':
        # print(dict(request.form))
        f = request.files['file']
        a = 'no file'
        if f.filename:
            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            a = app.config['UPLOAD_FOLDER'] + '\\' + f.filename
        l.createReq([a, dict(request.form)])
        return redirect(url_for('dashboard'))
    else:
        return render_template('createReq.html')


@app.route('/dashboard/<id>')
def requesUI(id):
    # return render_template('requestUI.html', data=[id, l.parseReqLog(id)])
    return jsonify([id, l.parseReqLog(id)])


@app.route('/dashboard/<id>/fetch')
def fetch(id):
    l.mailWalk(id)
    return render_template('requestUI.html', data=[id, l.parseReqLog(id)])


@app.route('/dashboard/<id>/download')
def download(id):
    path = pp.reports + '\{}.csv'.format(id)
    if not os.path.exists(path):
        mk.createReport(id)
    return send_file(path, as_attachment=True)


@app.route('/dashboard/<id>/delete')
def deleteReq(id):
    l.deleteReq(id)
    return redirect(url_for('dashboard'))


@app.route('/dashboard/<id>/edit', methods=['GET', 'POST'])
def editReq(id):
    if request.method == 'POST':
        f = request.files['file']
        a = 'no file'
        if f.filename:
            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            a = app.config['UPLOAD_FOLDER'] + '\\' + f.filename
        l.createReq([a, dict(request.form)])
        return redirect(url_for('dashboard'))
    else:
        d = l.parseReqLog(id)
        return render_template('editReq.html', d=[id, d])


if __name__ == '__main__':
    app.run(debug=True)
