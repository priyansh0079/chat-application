                            #By Ashwati shrimali

from flask import Flask, render_template,request,session
from flask_socketio import SocketIO,send
import user as u

Reg={}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        # myuser=u.User()
       Reg[Email]=request.form['Email Id']
       Reg[Password]=request.form['Password']
        cpassword=request.form['cPassword']
        myuser.firstname=request.form['User Id']
        # myuser.lastname=request.form['lastname']
        # myuser.prn=request.form['prn']
        if cpassword == Reg[Password]:
            # res =myuser.createuser()
            if len(Reg)>0:
                return render_template('login.html')

        else:
            return render_template('register.html')

print(Reg)



    return render_template('register.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatroom')
def sessions():
    return render_template('session.html')

                            #By Krutika deolapure

@app.route('/logout')
def logout():
    if 'response' in session:
        session.pop('response', None)
        session.pop('userName', None)

        return render_template('home.html');
    else:
        return '<p>user already logged out</p>'


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        myuser=u.User()

        myuser.email=request.form['email']
        myuser.password=request.form['password']
        res =myuser.validateUser()
        print(res)
        if res:
            session['response'] = res[1]
            session['userName'] = str(res[2])+" "  + str (res[3])
            x= session['userName']
            return render_template('session.html',name=x)

    return render_template('login.html')



def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    send(json,broadcast=True)
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)