def vueltasProgDin(listaValoresMonedas,vueltas,minMonedas,monedasUsadas):
   for centavos in range(vueltas+1):
      conteoMonedas = centavos
      nuevaMoneda = 1
      #En este ciclo consideramos el uso de todas las monedas posibles para
      #dar las vueltas por la cantidad especificada por centavos
      for j in [m for m in listaValoresMonedas if m <= centavos]:
            if minMonedas[centavos-j] + 1 < conteoMonedas:
               conteoMonedas = minMonedas[centavos-j]+1
               nuevaMoneda = j
      minMonedas[centavos] = conteoMonedas
      monedasUsadas[centavos] = nuevaMoneda
   return minMonedas[vueltas]

def imprimirMonedas(monedasUsadas,vueltas):
   moneda = vueltas
   while moneda > 0:
      estaMoneda = monedasUsadas[moneda]
      print(estaMoneda)
      moneda = moneda - estaMoneda

def main():
    #Las dos primeras líneas de main fijan la cantidad a convertir y
    #crean la lista de monedas usadas.
    cantidad = 63
    listaM = [1,5,10,21,25]
#líneas siguientes crean las listas que necesitamos para almacenar los resultados. 
    monedasUsadas = [0]*(cantidad+1)
#es el conteo de monedas usadas para dar el valor correspondiente a la posicion de la lista
    conteoMonedas = [0]*(cantidad+1)

    print("Dar unas vueltas de",cantidad,"centavos requiere")
    print(vueltasProgDin(listaM,cantidad,conteoMonedas,monedasUsadas),"monedas")
    print("Tales monedas son:")
    imprimirMonedas(monedasUsadas,cantidad)
    print("La lista usada es la siguiente:")
    print(monedasUsadas)

main()
