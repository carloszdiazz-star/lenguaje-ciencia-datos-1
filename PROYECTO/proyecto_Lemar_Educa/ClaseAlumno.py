class Alumno:
    def __init__(self, id_real, id_anonimo, grado, seccion,
                 titulo_lectura, palabras_texto, num_preguntas,
                 comprension_pct, tiempo_seg, velocidad_ppm):

        self.id_real = id_real
        self.id_anonimo = id_anonimo
        self.grado = grado
        self.seccion = seccion
        self.titulo_lectura = titulo_lectura
        self.palabras_texto = palabras_texto
        self.num_preguntas = num_preguntas
        self.comprension_pct = comprension_pct
        self.tiempo_seg = tiempo_seg
        self.velocidad_ppm = velocidad_ppm
        
    def __str__(self):
        return (
            f"{self.id_real} | Grado {self.grado}{self.seccion} | "
            f"Comprensión: {self.comprension_pct}% | "
            f"Velocidad: {self.velocidad_ppm} ppm"
        )


# 🆕 MÉTODO NUEVO
    def calcular_riesgo_lector(self):
        if self.comprension_pct < 50 or self.velocidad_ppm < 80:
            return "ALTO"
        elif self.comprension_pct < 75 or self.velocidad_ppm < 120:
            return "MEDIO"
        else:
            return "BAJO"
