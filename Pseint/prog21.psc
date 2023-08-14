Proceso sin_titulo
	Definir var1,var2,var3,var4 Como Real;
	Escribir "hora de entrada";
	Leer var1;
	Escribir "hora de salida";
	Leer var2;
	var3<--(var1-var2);
	var4<-35*var3;
	si var3>5 Entonces
		var4<-var4+20;
		si var3>8 Entonces
			var4<-var4+10;
		FinSi
	FinSi
	Escribir "su sueldo en total a recibir: ", var4;
FinProceso
