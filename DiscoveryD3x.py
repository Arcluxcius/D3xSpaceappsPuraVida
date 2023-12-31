#first of all please use pip install gmplot en cmd
#secondly use pip install pandas bokeh jupyter on your cmd
#import os
import gmplot
apikey = "AIzaSyAI9-DO8uYCgNtt59YXspjzmY38_wUAUCU"
gmap=gmplot.GoogleMapPlotter(9.9333300, -84.0833300,9, apikey=apikey)
#gmap.apikey = "AIzaSyAp7Bpm2VgQpqg4-7TyDmA-lxBPDQCH3Bw"
#gmap.draw("E:\SpaceApp\Mapas")
ZonaV1_Irazu = zip(*[(9.988120, -83.848201),
                     (9.992879, -83.854196),
                     (9.989581, -83.856724),
                     (9.986592, -83.858568),
                     (9.983010, -83.855697),
                     (9.978377, -83.854698),
                     (9.976315, -83.847769),
                     (9.982890, -83.842933)])
gmap.polygon(*ZonaV1_Irazu, color='gray', edge_width=8)
#Irazulats, Irazulong = zip(*[(9.981470697480898, -83.8467339066538)])
gmap.marker(9.981470697480898, -83.846733906653, color='red')
Zonvert_Nort = zip(*[(11.052843, -85.633484),(11.097131, -85.359272),
                      (10.962623, -85.158748),(10.916023, -84.895103),
                      (10.969414, -84.751386),
                      (11.069265, -84.699788),
                      (11.082080, -84.680250),
                      (11.050998, -84.631662),
                      (10.698827, -84.026025),(10.694013, -83.849648),
                      (10.230946, -83.925694),
                      (10.128111, -84.187832),
                      (10.675374, -85.047097),])
gmap.polygon(*Zonvert_Nort, color='cornflowerblue', edge_width=7)
Zonvert_Car = zip(*[(10.707645, -83.549323),
(10.449344, -83.458997),
(9.794572, -82.949886),
(9.695057, -82.820347),
(9.627456, -82.684915),
(9.583509, -82.602628),
(9.524340, -82.616342),
(9.546318, -82.679772),
(9.602103, -82.767203),
(9.635907, -82.859776),
(9.617315, -82.882062),
(9.561533, -82.894063),
(9.505741, -82.871776),
(9.480379, -82.948921),
(9.116272, -82.948635),
(9.296972, -83.110469),
(9.404301, -83.338629),
(9.438325, -83.450057),
(9.571191, -83.545469),
(9.775502, -83.910804),
(9.948549, -83.882702),
(10.124962, -83.865137),
(10.467133, -83.872163),
(10.535715, -83.811381)])
gmap.polygon(*Zonvert_Car, color='purple', edge_width=7)
Zonvert_Pacif = zip(*[(11.060670, -85.643685),(10.869164, -85.632377),(10.633082, -85.564527),
                      (10.310605, -85.742632),(9.946032, -85.592798),(9.848557, -85.225280),
                      (9.770068, -85.137105),(9.867665, -84.970082),(9.920970, -85.100889),
                      (10.080929, -85.274585),(10.243844, -85.298783),(10.157591, -85.038693),
                      (9.809560, -84.566574),(9.623604, -84.549487),(9.577736, -84.415216),
                      (9.329014, -83.927731),(9.050234, -83.544467),(8.801140, -83.554553),
                      (8.625039, -83.700416),(8.469473, -83.521741),(8.498287, -83.341123),
                      (8.722758, -83.511384),(8.801140, -83.356197),
                      (8.655641, -83.104174),(8.935212, -82.856982),(9.274209, -83.266223),
                      (9.417845, -83.582079),(9.845842, -84.012709),(9.914503, -83.985587),
                      (10.083740, -84.134142),(10.189386, -84.441991)])
gmap.polygon(*Zonvert_Pacif, color='green', edge_width=7)
#import pandas as pd 
#df =pd.read_excel ('statistics.xls')
gmap.draw('map.html')