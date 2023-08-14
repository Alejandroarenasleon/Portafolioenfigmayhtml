Proceso prog26
	definir val,contador,suma Como entero;
	Escribir "escribir un numero ";
	Leer val;
	contador<-0;
	suma<-0;
	Mientras val>=0 Hacer
		contador<-contador+1;
		suma<-suma+val;
		Escribir "positivo";
		leer val;
	FinMientras
    Escribir "fin del programa ";
	Escribir "numeros positivos ingresados ",contador;
	Escribir "suma de todos los positivos ", suma;
FinProceso
