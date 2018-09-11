from flask import Flask, render_template , request, redirect, url_for
from forms import paraForm
import paramiko

# Flask App

app = Flask(__name__)
app.config['SECRET_KEY'] = '123b123123bdfgdfgdsfsd123123'

# Flask Index

@app.route("/", methods = ["POST","GET"])
def index():
	form = paraForm()
	if request.method == "GET":
		return render_template("index.html",form=form)
	else:
		_user = request.form["user"]
		_passwd = request.form["passwd"]
		_destIp = request.form["destIp"]
		_command = request.form["command"]
		_result = ssh_connect(_destIp,_user,_passwd,_command)
		return render_template("index.html",result = _result, form=form)

# Paramiko Settings

def ssh_command(ssh,cmd):
    command = cmd
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout.read()

def ssh_connect(destIp, user, passwd,cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=destIp, username=user, password=passwd)
        return ssh_command(ssh,cmd)

# Flask Conf

if __name__=='__main__':
    app.run(debug=True)
