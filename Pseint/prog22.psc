Proceso prog22
		Definir a,b,c Como Entero;
		Leer a,b,c;
		Si a=b y a=c Entonces
			Escribir "Los tres valores son iguales";
		SiNo
			Si a<b Entonces
				Si a<c Entonces
					Escribir 'el menor es a';
				SiNo
					Escribir 'El menor es c';
				FinSi
			SiNo
				Si b<c Entonces
					Escribir 'el menor es b';
				SiNo
					Escribir 'El menor es c';
				FinSi
			FinSi
		FinSi
FinProceso