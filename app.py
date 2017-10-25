import pusher
from flask import Flask # requires `pip install flask`
from flask import render_template
from flask import request

pusher_client = pusher.Pusher(
  app_id='421068',
  key='bfb09ca7ed97d908bdac',
  secret='11c551666056c7e71073',
  cluster='ap2',
  ssl=True
)
app = Flask(__name__)

@app.route("/")
def show_index():
    return render_template('index.html')

@app.route("/notification", methods=['POST'])
def trigger_notification():
    message =  request.form['message']
    pusher_client.trigger('notifications', 'new_notification', {'message': message})
    return "Notification triggered!"

if __name__ == "__main__":
    app.run()
