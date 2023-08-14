Proceso prog28
	Definir val,contador Como Real;
	Escribir "ingrese un numero";
	Leer val;
	contador<-0;
	Mientras val>=1 Hacer
		val<- trunc(val/10);
		contador<-contador+1;
	FinMientras
	Escribir "el numero tiene ",contador," cifras";
FinProceso