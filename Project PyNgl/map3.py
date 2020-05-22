import Nio
import Ngl
import os,string,types

filename=os.path.join(Ngl.pynglpath("data"),"asc","fcover.dat")
data=Ngl.asciiread(filename,[3,73,73],"float")

wks_type="png"
wks=Ngl.open_wks(wks_type,"map3")

stres=Ngl.Resources()
cnres=Ngl.Resources()
mpres=Ngl.Resources()

cnres.nglDraw=False
cnres.nglFrame=False
mpres.nglDraw=False
mpres.nglFrame=False
stres.nglDraw=False
stres.nglFrame=False

cnres.sfXCStartV=-180.
cnres.sfXCEndV=180.
cnres.sfYCStartV=-90.
cnres.sfYCEndV=90.
stres.vfXCStartV=-180.
stres.vfXCEndV=180.
stres.vfYCStartV=-90.
stres.vfYCEndV=90.

stres.stLineColor="darkgreen"
cnres.cnLineColor="blue"
stres.stLineThicknessF=1.5
cnres.cnLineThicknessF=1.7
cnres.cnLineDashPattern=7
cnres.cnLineLabelsOn=False

mpres.mpGridAndLimbOn=False
mpres.mpCenterLatF=90.0
mpres.mpCenterLonF=180.0
mpres.mpCenterRotF=45.0
mpres.mpFillOn=True
mpres.mpGridAndLimbDrawOrder="Draw"
mpres.mpGridLineDashPattern=5
mpres.mpInlandWaterFillColor="transparent"
mpres.mpOceanFillColor="transparent"
mpres.mpLandFillColor="tan"
mpres.mpLabelsOn=False
mpres.mpLeftCornerLatF=10.
mpres.mpLeftCornerLonF=-180.
mpres.mpLimitMode="corners"
mpres.mpProjection="Stereographic"
mpres.mpRightCornerLatF=10.
mpres.mpRightCornerLonF=0.

stream=Ngl.streamline(wks,data[0,:,:],data[1,:,:],stres)
contour=Ngl.contour(wks,data[2,:,:],cnres)
map=Ngl.map(wks,mpres)

Ngl.overlay(map,stream)
Ngl.overlay(map,contour)

Ngl.maximize_plot(wks,map)

del cnres.nglDraw
del cnres.nglFrame
del mpres.nglDraw
del mpres.nglFrame
del stres.nglDraw
del stres.nglFrame

resources=Ngl.Resources()

for res in [cnres, mpres, stres]:
    d = res.__dict__
    resources.__dict__.update({key: d[key] for key in d if res is not cnres or (len(key) > 5 and key[0:6] != 'cnLine')})

resources.mpLimitMode="LatLon"
resources.mpMinLatF= 20
resources.mpMaxLatF= 85
resources.mpMinLonF=-30
resources.mpMaxLonF=60.

resources.stMonoLineColor=False
resources.stLineThicknessF=1.7
resources.tiMainString="Streamlines colored by scalarfield"

stream=Ngl.streamline_scalar_map(wks,data[0,:,:],data[1,:,:],data[2,:,:],resources)
Ngl.end()
