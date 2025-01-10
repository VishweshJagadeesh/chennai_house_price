from flask import Flask, request, jsonify
import util

app=Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    util.load_saved_artifacts()
    resp=jsonify({
        'locations': util.get_location_names()
    })
    resp.headers.add('Access-Control-Allow-Origin','*')
    return resp

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    util.load_saved_artifacts()
    area=request.form['area']
    sale_cond=request.form['sale_cond']
    park_facil=float(request.form['park_facil'])
    utility_avail=request.form['utility_avail']
    buildtype=request.form['buildtype']
    street=request.form['street']
    mzzone=request.form['mzzone']
    property_age=float(request.form['property_age'])
    int_sqft=float(request.form['int_sqft'])
    n_bedroom=float(request.form['n_bedroom'])
    n_bathroom=float(request.form['n_bathroom'])
    n_room=float(request.form['n_room'])

    resp=jsonify({
        'estimated_price':util.get_estimated_price(area,sale_cond,park_facil,buildtype,utility_avail,street,mzzone,property_age,int_sqft,n_bedroom,n_bathroom,n_room)
    })
    resp.headers.add('Access-Control-Allow-Origin','*')
    return resp

#area,sale_cond,park_facil,buildtype,utility_avail,street,mzzone,property_age,int_sqft,n_bedroom,n_bathroom,n_room
if __name__=='__main__':
    print("works")
    app.run()