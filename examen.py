peliculas={
'P101':['Luz de Otoño','drama',110,'B','Español',False],
'P102':['Noche Neón','acción',125,'C','Ingles',True],
'P103':['Planeta Agua','documental',90,'A','Español',False],
'P104':['Risa Total','comedia',105,'A','Español',True],
'P105':['Código Zero','thriller',118,'C','Ingles',True],
'P106':['Viaje Lunar','ciencia ficción',132,'B','Ingles',False]
}
cartelera={
'P101':[5990,40],'P102':[7990,0],'P103':[4990,25],
'P104':[6990,12],'P105':[8990,8],'P106':[7490,3]
}
def validartexto(x): return x.strip()!=""
def validarcodigo(c): return validartexto(c)
def validartitulo(t): return validartexto(t)
def validargenero(g): return validartexto(g)
def validarduracion(d): return isinstance(d,int) and d>0
def validarclasificacion(c): return c in ["A","B","C"]
def validaridioma(i): return validartexto(i)
def validar3d(v): return v.lower() in ["s","n"]
def validarprecio(p): return isinstance(p,int) and p>0
def validarcupos(c): return isinstance(c,int) and c>=0
def buscarcodigo(c):
    c=c.upper()
    for k in peliculas:
        if k.upper()==c: return k
    return None
def cuposgenero(g):
    t=0
    for k,v in peliculas.items():
        if v[1].lower()==g.lower():
            t+=cartelera[k][1]
    print("El total de cupos disponibles es:",t)
def busquedaprecio(a,b):
    r=[]
    for k,v in cartelera.items():
        if a<=v[0]<=b and v[1]>0:
            r.append(f"{peliculas[k][0]}--{k}")
    if r:
        r.sort()
        print(r)
    else:
        print("No hay películas con ese rango de precios.")
def actualizarprecio(c,p):
    k=buscarcodigo(c)
    if not k:return False
    cartelera[k][0]=p
    return True
def agregarpelicula(c,t,g,d,cl,i,e,p,cu):
    if buscarcodigo(c): return False
    peliculas[c]=[t,g,d,cl,i,e]
    cartelera[c]=[p,cu]
    return True
def eliminarpelicula(c):
    k=buscarcodigo(c)
    if not k:return False
    del peliculas[k]; del cartelera[k]
    return True
while True:
    print("========== MENÚ PRINCIPAL ==========")
    print ("1. Cupos por género")
    print ("2. Búsqueda de películas por rango de precio")
    print ("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
    op=input("Ingrese opción: ")
    if op=="1":
        cuposgenero(input("Ingrese género: "))
    elif op=="2":
        while True:
            try:
                mi=int(input("Precio mínimo: "))
                ma=int(input("Precio máximo: "))
                break
            except:
                print("Debe ingresar valores enteros")
        busquedaprecio(mi,ma)
    elif op=="3":
        while True:
            c=input("Código: ")
            p=int(input("Nuevo precio: "))
            print("Precio actualizado" if actualizarprecio(c,p) 
                  else "El código no existe")
            if input("¿Desea actualizar otro precio (s/n)?: ").lower()=="n": break
    elif op=="4":
        c=input("Código: ").upper()
        t=input("Título: "); g=input("Género: ")
        d=int(input("Duración: "))
        cl=input("Clasificación: ").upper()
        i=input("Idioma: ")
        e=input("¿Es 3D? (s/n): ").lower()
        price=int(input("Precio: "))
        cu=int(input("Cupos: "))
        if not(validarcodigo(c) and validartitulo(t) and validargenero(g) and validarduracion(d)
               and validarclasificacion(cl) and validaridioma(i) and validar3d(e)
               and validarprecio(p) and validarcupos(cu)):
            print("Datos inválidos")
        else:
            ok=agregarpelicula(c,t,g,d,cl,i,e=="s",p,cu)
            print("Película agregada" if ok 
                  else "El código ya existe")
    elif op=="5":
        print("Película eliminada" if eliminarpelicula(input("Código: ")) 
              else "El código no existe")
    elif op=="6":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida")
