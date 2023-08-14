Proceso prog27
	Definir val,suma,suma1,suma2, promedio,promedio1,promedio2,contador,contador1,contador2 Como real;
	Escribir "escribir un numero ";
	Leer val;
	contador<-0;
	contador1<-0;
	contador2<-0;
	suma<-0;
	suma1<-0;
	suma2<-0;
	Mientras val>=0 y val<=100 Hacer
		si val<=18 Entonces
			contador<-contador+1;
			suma<-suma+val;
			Escribir "niño";
		SiNo
			si	val>18 y val<60 Entonces
				contador1<-contador1+1;
				suma1<-suma1+val;
				Escribir "adulto";
			SiNo
				si val>=61 y val<=100 Entonces
					contador2<-contador2+1;
					suma2<-suma2+val;
					Escribir "anciano";
				FinSi
			FinSi
		FinSi
		Leer val;
	FinMientras
	promedio<-suma/contador;
	promedio1<-suma1/contador1;
	promedio2<-suma2/contador2;
	Escribir "suma de veces ingresados: ",contador;
	Escribir "suma de veces ingresados: ",contador1;
	Escribir "suma de veces ingresados: ",contador2;
	Escribir "promedio ",promedio;
	Escribir "promedio",promedio1;
	Escribir "promedio",promedio2;
	Escribir "suma de todos los positivos ", suma;
FinProceso

