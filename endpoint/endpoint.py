import sys
sys.path.append('../')
from gap_python.gap_python import ITCP
t = ITCP()
out = t.__execfunction__("b:=[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ];")
print(out)
from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
@app.route('/itcpendpoint', methods=['POST'])
@cross_origin()
def itcpendpoint():
	if request.method != 'POST':
		return "This endpoint only supports POST"
	data = request.get_json()
	print(data)
	function = data['function']
	data = data['idsc']
	return executefunction(function, data)
def executefunction(func, data):
	if func.lower() == "netsymgroup":
		return t.__execfunction__("G:=NetSymGroup("+str(data)+");")
	elif func.lower() == "ncrateregionob":
		return t.__execfunction__("rlist1:=NCRateRegionOB2("+str(data)+",true,[]);;Display(rlist1[2]);")

if __name__ == '__main__':
    app.run(debug=True, port=5000)