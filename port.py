from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def app():
    def check_name(data):
        if len(data['user']) > 20:
            return('user','اسم المشترك طويل')

    popup('اهلا وسهلا',
    put_text(' اهلا وسهلا صديقي العزيز هذا الموقع تجريبي لا تقم بأدخال معلومات حقيقيةعنك مثل كلمة السر او البريد الالكتروني').onclick(lambda:toast('مثل ماكتلك🙂')) )
    put_html('<center><h3>نظام تسجيل الدخول</h3><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width=150></center>')
    data=input_group('مشترك جديد',
    [
        input('اسم المشترك', name='user'),
         input('كلمة السر', name='pass',type=PASSWORD)
    ], validate=check_name
    )
    put_text('معلومات المشترك الجديد').style('color:red')
    put_text('user name : %r' % data['user'])
    put_text('password : %r' % data['pass'])
   
start_server(app, port=5667 , debug=True)