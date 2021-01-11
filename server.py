from flask import Flask, redirect, render_template, request
from netmiko import ConnectHandler

app = Flask(__name__)
app.config["DEBUG"] = True

result = ''

def send_show_command(ip, username, password, command, port, secret=''): 
    with ConnectHandler(device_type= "cisco_ios", ip=ip, port=port, username=username, password=password, secret = secret) as ssh:
        ssh.enable()
        global result
        result = ssh.send_command(command)
    return result

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        if 'get_ver' in request.form:
            ip = request.form['ip']
            port = request.form['port']
            login = request.form['login']
            password = request.form['password']
            secret = request.form['secret']
            send_show_command(ip, login, password, 'sh ver', port, secret)
            return redirect('/info')

        elif 'get_start_conf' in request.form:
            ip = request.form['ip']
            port = request.form['port']
            login = request.form['login']
            password = request.form['password']
            secret = request.form['secret']
            send_show_command(ip, login, password, 'sh start', port, secret)
            return redirect('/info')

        elif 'get_cur_conf' in request.form:
            ip = request.form['ip']
            port = request.form['port']
            login = request.form['login']
            password = request.form['password']
            secret = request.form['secret']
            send_show_command(ip, login, password, 'sh run', port, secret)
            return redirect('/info')

        elif 'get_acl' in request.form:
            ip = request.form['ip']
            port = request.form['port']
            login = request.form['login']
            password = request.form['password']
            secret = request.form['secret']
            send_show_command(ip, login, password, 'sh access-lists', port, secret)
            return redirect('/info')

        elif 'get_int' in request.form:
            ip = request.form['ip']
            port = request.form['port']
            login = request.form['login']
            password = request.form['password']
            secret = request.form['secret']
            send_show_command(ip, login, password, 'sh ip int br', port, secret)
            return redirect('/info')

@app.route('/info')
def ver():
    global result
    result = result.splitlines()
    result = '<br>'.join(result)
    return result

app.run(host='0.0.0.0')