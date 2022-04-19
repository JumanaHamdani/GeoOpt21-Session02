
#Import libraries
from flask import Flask
import ghhops_server as hs
import random as r
import rhino3dm as rg

#Add hops as middleware
app = Flask(__name__)
hops = hs.Hops(app)

#create docoration, inputs, outputs
@hops.component(
    "/pointat",
    name = "Point in Wavey Curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t","t", "Parameter on Curve to evaluate", default=1.0)                  
    ],

    outputs=[
       hs.HopsPoint("Point","P","Point on Curve at t")    
    ]

#create function  
)
def pointat(curve:rg.Curve, t:float):
    return curve.PointAt(t)

if __name__== "__main__":
    app.run(debug=True)