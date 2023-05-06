from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/cart/store', methods=['POST'])
def cart_store():
   output = request.get_json()
   result = json.loads(output)
   print(result)

   return json.dumps({'success':True}), 200, {'ContentType':'application/json'}









if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)