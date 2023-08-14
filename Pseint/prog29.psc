Proceso pro29
	Definir val,contador,divisores Como Real;
	Escribir "ingrese un numero";
	Leer val;
	contador<-0;
	divisores<-0;
	si val<=0 Entonces
		Escribir "el numero tiene que ser mayor que cero ";
	SiNo
		divisores<-0;
		contador<-1;
		mientras contador<= val Hacer
			si val	mod contador=0 Entonces
				divisores<-divisores+1;
			FinSi
			contador<-contador+1;
		FinMientras
		si divisores=2 Entonces
			Escribir "numero primo";
		SiNo
			Escribir "numero no primo";
			
		FinSi
		
	FinSi
FinProceso
