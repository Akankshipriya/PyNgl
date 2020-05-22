import Ngl,Nio,os
from scipy.ndimage import gaussian_filter
import xarray as xr
from metpy.units import units
import metpy.calc as mpcalc
from datetime import datetime

ds = xr.open_dataset('NAM_20161031_1200.nc')



lats = ds.lat.data
lons = ds.lon.data

hght = ds['Geopotential_height_isobaric']
uwnd = ds['u-component_of_wind_isobaric']
temp = ds['Temperature_isobaric'][0][0]

hght_850 = gaussian_filter(hght.sel(isobaric=850).data[0], sigma=1.0)
uwnd_850 = gaussian_filter(uwnd.sel(isobaric=850).data[0], sigma=1.0) * units('m/s')
temp=(temp-273.15)*9.0/5.0+32.0


wkresource=Ngl.Resources()
wkresource.wkWidth=2500
wkresource.wkHeight=2500
wks_type="png"
wks_name=os.path.basename(__file__).split(".")[0]
wks=Ngl.open_wks(wks_type,wks_name,wkresource)

resource=Ngl.Resources()

resource.mpLimitMode="LatLon"
resource.mpMinLatF= 20
resource.mpMaxLatF= 85
resource.mpMinLonF=-30
resource.mpMaxLonF=60.

resource.mpFillOn=True

resource.mpGridMaskMode="MaskNotOcean"
resource.mpGridLineDashPattern=2

resource.mpGridLatSpacingF       = 1
resource.mpGridLonSpacingF       = 1
resource.stLineThicknessF  = 3.0
resource.stMonoLineColor   = False


cmap=Ngl.read_colormap_file("rainbow+gray")
resource.vcLevelPalette=cmap[0:20]


resource.mpOceanFillColor="Transparent"
resource.mpLandFillColor="Tan"

resource.mpFillBoundarySets    = "National"

resource.tiMainString="~F25~Temperature and Wind"

resource.lbTitleString="TEMPERATURE(~S~o~N~F)"
resource.lbTitleFontHeightF=0.010
resource.lbBoxMinorExtentF=0.18

resource.vfXArray=lons[0]
resource.vfYArray=lats[0]

stream=Ngl.streamline_scalar_map(wks,temp,uwnd_850,hght_850,resource)
Ngl.end()
