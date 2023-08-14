Proceso prog30
	Definir val,contador,divisores Como Real;
	Escribir 'ingrese un numero';
	Leer val;
	divisores <- 0;
	contador <- 1;
	Mientras contador<=val Hacer
		Si val MOD contador=0 Entonces
			divisores <- divisores+1;
		FinSi
		contador <- contador+1;
	FinMientras
	Si divisores=2 Entonces
		Escribir 'numero primo';
	SiNo
		Escribir 'numero no primo';
	FinSi
FinProceso
