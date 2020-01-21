import numpy as np 

cw = 4.18000
mh = 287.58
mk = 273.24
Th = 80.0000+273.15
Tk = 21.8000+273.15
Tm = 47.3000+273.15


print(Th)
print(Tk)
print(Tm)
#print((cw*((mh*(Th-Tm))-mk*(Tm-Tk)))/(Tm-Tk))


x = [23.19,25.35,22.38]
print(np.std(x))

#print( ((cW * mW + cG * mG) (Tv-Tw))(Tp-Tv)    )
