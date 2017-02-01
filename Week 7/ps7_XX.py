alist = []
Nx = 6
roa = 3

if Nx%2 == 0:
    for i in range(-Nx,Nx+1,2):
        if i !=0:
            alist += [roa*float(i)/Nx]
else:
    Nx = Nx-1
    for i in range(-Nx,Nx+1,2):
        alist += [roa*float(i)/Nx]

print alist