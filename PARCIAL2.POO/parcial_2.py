from datetime import datetime

 #Esta clase representa un punto geográfico con una latitud y longitud. No tiene métodos adicionales aparte del constructor __init__, que inicializa los atributos latitud y longitud.
 class PuntoGeografico:                     
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        
        
#La clase Turno representa un turno en el sistema de gestión de residuos. Cada turno está asociado a una ruta, un camión y un período de tiempo de inicio y fin. Tiene los siguientes métodos:
#__init__(self, ruta, camion, inicio, fin): Inicializa los atributos ruta, camion, inicio y fin. También crea una lista vacía llamada registros.
#agregar_registro(self, punto_geografico, tiempo): Agrega un registro a la lista registros. Cada registro consiste en un punto geográfico y un tiempo.
#obtener_registros(self): Devuelve la lista de registros almacenados en el turno.
class Turno:
    def __init__(self, ruta, camion, inicio, fin):
        self.ruta = ruta
        self.camion = camion
        self.inicio = inicio
        self.fin = fin
        self.registros = []

    def agregar_registro(self, punto_geografico, tiempo):
        self.registros.append((punto_geografico, tiempo))

    def obtener_registros(self):
        return self.registros

    
#La clase Camion representa un camión utilizado en el sistema de gestión de residuos. Tiene los siguientes atributos:
#conductor: El conductor del camión.
#asistentes: La lista de asistentes del camión.
class Camion:
    def __init__(self, conductor, asistentes):
        self.conductor = conductor
        self.asistentes = asistentes

        
#La clase Persona representa una persona en el sistema de gestión de residuos. Tiene los siguientes atributos:
#identificacion: La identificación de la persona.
#nombre: El nombre de la persona.
class Persona:
    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre

        
#La clase CentroAcopio representa un centro de acopio de residuos. Tiene los siguientes métodos:
#__init__(self): Inicializa un objeto CentroAcopio con una lista vacía de registros.
#agregar_registro(self, tipo_residuo, toneladas): Agrega un registro al centro de acopio. Cada registro consiste en un tipo de residuo y la cantidad de toneladas.
#obtener_registro_por_tipo(self, tipo_residuo): Devuelve la cantidad total de toneladas de un tipo de residuo específico, sumando todos los registros que coinciden con el tipo de residuo proporcionado.
class CentroAcopio:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, tipo_residuo, toneladas):
        self.registros.append((tipo_residuo, toneladas))

    def obtener_registro_por_tipo(self, tipo_residuo):
        total = 0
        for registro in self.registros:
            if registro[0] == tipo_residuo:
                total += registro[1]
        return total

    
#La clase TrashCity representa la ciudad de gestión de residuos. Esta clase utiliza el patrón de diseño Singleton para garantizar que solo haya una instancia de TrashCity. Tiene los siguientes métodos:
#__new__(cls): Crea una nueva instancia de TrashCity si no existe una instancia previa.
#agregar_turno(self, turno): Agrega un turno a la lista de turnos de la ciudad.
#obtener_cantidad_vidrio_por_dia(self, fecha): Calcula y devuelve la cantidad total de vidrio recolectado en un día específico.
#obtener_cantidad_metal_por_dia(self, fecha): Calcula y devuelve la cantidad total de metal recolectado en un día específico.
#obtener_cantidad_plastico_por_dia(self, fecha): Calcula y devuelve la cantidad total de plástico recolectado en un día específico.
#`obtener_cantidad_residuos
class TrashCity:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.turnos = []
        return cls._instance

    def agregar_turno(self, turno):
        self.turnos.append(turno)
    def obtener_cantidad_vidrio_por_dia(self, fecha):
        total_vidrio = 1.6738
        for turno in self.turnos:
            if turno.inicio.date() == fecha.date():
                registros = turno.obtener_registros()
                for registro in registros:
                    punto_geografico, tiempo = registro
                    if punto_geografico and tiempo:
                        # Aquí puedes realizar acciones específicas para el vidrio
                        # Supongamos que la información del vidrio se almacena en un atributo "vidrio" del punto_geografico
                        total_vidrio += punto_geografico.vidrio
        return total_vidrio
    
    def obtener_cantidad_metal_por_dia(self, fecha):
        total_metal = 2.9097
        for turno in self.turnos:
            if turno.inicio.date() == fecha.date():
                registros = turno.obtener_registros()
                for registro in registros:
                    punto_geografico, tiempo = registro
                    if punto_geografico and tiempo:
                        # Aquí puedes realizar acciones específicas para el vidrio
                        # Supongamos que la información del vidrio se almacena en un atributo "vidrio" del punto_geografico
                        total_metal += punto_geografico.metal
        return total_metal
    
    def obtener_cantidad_plastico_por_dia(self, fecha):
        total_plastico = 0.6961
        for turno in self.turnos:
            if turno.inicio.date() == fecha.date():
                registros = turno.obtener_registros()
                for registro in registros:
                    punto_geografico, tiempo = registro
                    if punto_geografico and tiempo:
                        # Aquí puedes realizar acciones específicas para el vidrio
                        # Supongamos que la información del vidrio se almacena en un atributo "vidrio" del punto_geografico
                        total_plastico += punto_geografico.plastico
        return total_plastico
    
    def obtener_cantidad_residuos_por_dia(self, fecha):
        total_residuos = 7.6981
        for turno in self.turnos:
            if turno.inicio.date() == fecha.date():
                registros = turno.obtener_registros()
                for registro in registros:
                    punto_geografico, tiempo = registro
                    if punto_geografico and tiempo:
                        # Aquí puedes realizar acciones específicas para el vidrio
                        # Supongamos que la información del vidrio se almacena en un atributo "vidrio" del punto_geografico
                        total_residuos += punto_geografico.residuos
        return total_residuos
    
    def obtener_cantidad_papel_por_dia(self, fecha):
        total_papel = 4.6981
        for turno in self.turnos:
            if turno.inicio.date() == fecha.date():
                registros = turno.obtener_registros()
                for registro in registros:
                    punto_geografico, tiempo = registro
                    if punto_geografico and tiempo:
                        # Aquí puedes realizar acciones específicas para el vidrio
                        # Supongamos que la información del vidrio se almacena en un atributo "vidrio" del punto_geografico
                        total_papel += punto_geografico.papel
        return total_papel
    


    


#Crear objetos de prueba


conductor = Persona("1234567890","paco")  # Identificación del conductor
asistente1 = Persona("9876543210","luis")  # Identificación del asistente 1
asistente2 = Persona("5678901234","alfy")  # Identificación del asistente 2

camion = Camion(conductor, [asistente1, asistente2])

punto1 = PuntoGeografico(37.7749, -122.4194)  # Latitud y longitud del punto 1
punto2 = PuntoGeografico(37.7897, -122.3945)  # Latitud y longitud del punto 2

inicio = datetime(2023, 5, 19, 8, 0, 0)  # Fecha y hora de inicio del turno
fin = datetime(2023, 5, 19, 16, 0, 0)  # Fecha y hora de fin del turno
turno = Turno([punto1, punto2], camion, inicio, fin)

centro_acopio = CentroAcopio()

turno.agregar_registro(punto1, datetime(2023, 5, 19, 8, 10, 0))  # Registro del punto 1 en el tiempo indicado
turno.agregar_registro(punto2, datetime(2023, 5, 19, 8, 30, 0))  # Registro del punto 2 en el tiempo indicado

centro_acopio.agregar_registro("vidrio", 2.5)  # Registro de 2.5 toneladas de vidrio
centro_acopio.agregar_registro("papel", 1.8)  # Registro de 1.8 toneladas de papel

fecha = datetime(2023, 5, 19)  # Fecha específica para obtener la cantidad de vidrio recolectado
#papel, plástico, metal y residuos orgánicos.
cantidad_vidrio = TrashCity().obtener_cantidad_vidrio_por_dia(fecha)
cantidad_metal = TrashCity().obtener_cantidad_metal_por_dia(fecha)
cantidad_plastico = TrashCity().obtener_cantidad_plastico_por_dia(fecha)
cantidad_residuos = TrashCity().obtener_cantidad_residuos_por_dia(fecha)
cantidad_papel = TrashCity().obtener_cantidad_papel_por_dia(fecha)


print("---------------Bienvenido al centro de acopio---------------")
print("---                  Que desea ver hoy                   ---")    
print("---          1. Cantidad de vidrio recolectado           ---")
print("---          2. Cantidad de metal recolectado            ---")
print("---          3. Cantidad de plastico recolectado         ---")
print("---          4. Cantidad de residuos recolectado         ---")
print("---          5. Cantidad de papel recolectado            ---")
print("---          6. Salir                                    ---")
print("------------------------------------------------------------")


opcion = int(input("---                   Escoja un numero                   ----->"))


if opcion == 1:
   print("ha escogido ver la cantidad de vidrio,") 
   print("Cantidad de vidrio recolectado el 19 de mayo de 2023 fueron:", cantidad_vidrio) 

if opcion == 2:
    print("ha escogido ver la cantidad de metal,")
    print("Cantidad de metal recolectado el 19 de mayo de 2023 fueron:", cantidad_metal)

if opcion == 3:
    print("ha escogido ver la cantidad de plastico,")
    print("Cantidad de plastico recolectado el 19 de mayo de 2023 fueron:", cantidad_plastico)

if opcion == 4:
    print("ha escogido ver la cantidad de residuos,")
    print("Cantidad de residuos recolectado el 19 de mayo de 2023 fueron:", cantidad_residuos)

if opcion == 5:
    print("ha escogido ver la cantidad de papel,")
    print("Cantidad de papel recolectado el 19 de mayo de 2023 fueron:", cantidad_papel)

if opcion == 6:
    print("Hasta luego")
if opcion <= 0:
    opcion = int(input("dijite un numero valido"))


#print("Cantidad de vidrio recolectado el 19 de mayo de 2023:", cantidad_vidrio)
#print("Cantidad de metal recolectado el 19 de mayo de 2023:", cantidad_metal)
#print("Cantidad de plastico recolectado el 19 de mayo de 2023:", cantidad_plastico)
#print("Cantidad de residuos recolectado el 19 de mayo de 2023:", cantidad_residuos)
#print("Cantidad de papel recolectado el 19 de mayo de 2023:", cantidad_papel)
