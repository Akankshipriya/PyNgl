import Ngl
import Nio
import numpy
import os
dirc=Ngl.pynglpath("data")
file=Nio.open_file(os.path.join(dirc,"cdf","pop.nc"))

wks_type="png"
wks=Ngl.open_wks(wks_type,"map2")

urot=file.variables["urot"]
t=file.variables["t"]
lat2d=file.variables["lat2d"]
lon2d=file.variables["lon2d"]


u=Ngl.add_cyclic(urot[:])
temp=Ngl.add_cyclic(t[0:])
lon=Ngl.add_cyclic(lon2d[0:])
lat=Ngl.add_cyclic(lat2d[0:])


resource=Ngl.Resources()

resource.vfXArray=lon
resource.vfYArray=lat

resource.mpProjection="Stereographic"
resource.mpFillOn=True
resource.mpInlandWaterFillColor="SkyBlue"
resource.mpProjection          = "Stereographic"
resource.mpEllipticalBoundary  = True

resource.mpLimitMode           = "LatLon"   # Specify area of map
resource.mpMaxLatF             = 90.        # to zoom in on.
resource.mpMinLatF             = 30
resource.mpCenterLatF          = 90.
resource.mpOutlineOn           = False
resource.mpGridLineDashPattern = 2

resource.mpDataBaseVersion="MediumRes"

resource.vfXArray=lon[::3,::3]
resource.vfYArray=lat[::3,::3]
resource.vcRefLengthF=0.1

resource.vfXArray=lon
resource.vfYArray=lat

resource.vcRefLengthF=0.08
resource.vcMinFracLengthF=0.1
resource.vcMinDistanceF=0.013

cmap=Ngl.read_colormap_file("rainbow+gray")
resource.vcLevelPalette=cmap[22:236]

resource.mpOceanFillColor="Transparent"
resource.mpLandFillColor="Tan"

resource.mpFillBoundarySets    = "National"

resource.tiMainString="Northen Hemishapre"

map=Ngl.vector_map(wks,u,temp,resource)
Ngl.end()
