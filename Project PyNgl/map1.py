import Ngl,Nio,os
diri="./"
fname="rectilinear_grid_2D.nc"
f=Nio.open_file(os.path.join(diri,fname),"r")
temp=f.variables["tsurf"][0,:,:]
u=f.variables["u10"][0,:,:]
v=f.variables["v10"][0,:,:]
lat=f.variables["lat"][:]
lon=f.variables["lon"][:]

nlon=len(lon)
nlat=len(lat)


wkresource=Ngl.Resources()
wkresource.wkWidth=2500
wkresource.wkHeight=2500
wks_type="png"
wks_name=os.path.basename(__file__).split(".")[0]
wks=Ngl.open_wks(wks_type,wks_name,wkresource)

resource=Ngl.Resources()

tempa=(temp-273.15)*9.0/5.0+32.0

resource.mpLimitMode="LatLon"
resource.mpMinLatF=18.0
resource.mpMaxLatF=65.0
resource.mpMinLonF=-128.
resource.mpMaxLonF=-58.

resource.mpFillOn=True
resource.mpLandFillColor="gray45"
resource.mpOceanFillColor="transparent"
resource.mpInlandWaterFillColor="transparent"
resource.mpGridMaskMode="MaskNotOcean"
resource.mpGridLineDashPattern=2
resource.mpOutlineBoundarySets="GeophysicalAndUSStates"

resource.vcFillArrowsOn=True
resource.vcMonoFillArrowFillColor=False
resource.vcFillArrowEdgeColor="black"
resource.vcLineArrowColor="black"
resource.vcGlyphStyle="CurlyVector"
resource.vcLineArrowThicknessF=5.0

resource.tiMainString="~F25~Temperature and Wind"

resource.lbTitleString="TEMPERATURE(~S~o~N~F)"
resource.lbTitleFontHeightF=0.010
resource.lbBoxMinorExtentF=0.18

resource.vfXArray=lon
resource.vfYArray=lat

map=Ngl.vector_scalar_map(wks,u,v,tempa,resource)
Ngl.end()
