
#declaracion de variables a utilizar
def vueltasRecB(listaValoresMonedas,vueltas,resultadosConocidos):
   minMonedas = vueltas

   #aqui se esta verificando nuestro caso base; es decir, estamos tratando de dar las vueltas correspondientes a la cantidad exacta de una de nuestras monedas. Si no tenemos una moneda igual a
   #la cantidad de las vueltas, hacemos llamadas recursivas para cada valor de
   #moneda diferente menor que la cantidad de las vueltas que estamos tratando de generar.
   
   if vueltas in listaValoresMonedas:
      resultadosConocidos[vueltas] = 1
      return 1
   elif resultadosConocidos[vueltas] > 0:
      return resultadosConocidos[vueltas]

#muestra cómo filtramos la lista de monedas a aquéllas que sean menores que el valor actual de las vueltas usando una comprensión de listas. La llamada recursiva también reduce la
#cantidad total de las vueltas que necesitamos generar con el valor de la moneda seleccionada.
#tambien se hace la llamada recursiva
   else:
       for i in [m for m in listaValoresMonedas if m <= vueltas]:
         numeroMonedas = 1 + vueltasRecB(listaValoresMonedas, vueltas-i,
                              resultadosConocidos)
         if numeroMonedas < minMonedas:
            minMonedas = numeroMonedas
            resultadosConocidos[vueltas] = minMonedas
   return minMonedas

print(vueltasRecB([1,5,10,25],63,[0]*64))
