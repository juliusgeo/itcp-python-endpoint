import sys
sys.path.append('../')
from gap_python import ITCP
t = ITCP()
out = t.__execfunction__("rlist:=NCRateRegionOB([[[ [ 1, 2 ], [ 1, 2, 4 ] ], [ [ 2, 3 ], [ 2, 3, 5 ] ],[ [ 4, 5 ], [ 4, 5, 6 ] ], [ [ 3, 4 ], [ 3, 4, 7 ] ],[ [ 1, 6 ], [ 3, 1, 6 ] ], [ [ 6, 7 ], [ 2, 6, 7 ] ],[ [ 5, 7 ], [ 1, 5, 7 ] ] ], 3, 7 ],true,[]);;")
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
		t.__execfunction__("rlist1:=NCRateRegionOB2("+str(data)+",true,[]);;Display(rlist1[2]);")
		return t.__execfunction__("Display(rlist[2]);")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)