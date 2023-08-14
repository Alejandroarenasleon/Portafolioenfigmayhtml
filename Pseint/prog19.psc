Proceso prog19
	Definir var1,var2,var3 Como Real;
	Escribir "ingrese su promedio";
	Leer var1;
	Escribir "ingrese su estatura ";
	Leer var2;
	Escribir "ingrese su ";
	Leer var3;
	
	si var1>=60 y var2>=1.70 y var3>=100 Entonces
		Escribir "puede ingresar a la Universidad por los 2 metodos ";
	SiNo
		si var1>=60 y var2>=1.70 y var3<100 Entonces
			Escribir "puede imgresar ah la universidad por el primer metodo";
		SiNo
			si var1<60 y var2<1.70 y var3>=100 Entonces
				Escribir "puede ingresar a la Universida por el segundo metodo";
			SiNo
				Escribir "no puede ingresar a la Universidad por ningun metodo";
			FinSi
		FinSi
	FinSi
FinProceso
