from flask import Flask, render_template, request
import datetime
from script import getSong

app = Flask(__name__)

@app.route('/')
def index():
	#now = datetime.datetime.now()
	#timeStringg = now.strftime('%Y-%m-%d %H:%M')
	templateData = {
		'title': 'Young carti, young carti',
		'v1'  :  'verse1',
		'ch1' :  'chorus',
		'v2'  :  'verse2',
		'ch2' :  'chorus',
		'v3'  :  'verse3'
	}
	return render_template('index.html', **templateData)

@app.route('/carti')
def action():
	t,c,v1,v2,v3 = getSong()
	
	#c=c.replace('\n','<br>')
	c = c.split('\n')
	#v1=v1.replace('\n','<br>')
	v1 = v1.split('\n')
	#v2=v2.replace('\n','<br>')
	v2 = v2.split('\n')
	#v3=v3.replace('\n','<br>')
	v3 = v3.split('\n')
	#print(v3)

	templateData = {
		'title': t,
		'v1'  :  v1,
		'ch1' :  c,
		'v2'  :  v2,
		'ch2' :  c,
		'v3'  :  v3
	}
	return render_template('index.html', **templateData)




if __name__=='__main__':
	app.run(host='0.0.0.0', port=80, debug=True)

