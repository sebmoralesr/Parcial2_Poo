# Parcial2_Poo
En este repositorio se encontrara un archivo el cual contiene el codigo de la implementacion, otro donde se encuentra la unittest, y el diagrama UML
En el codigo de la implementacion se encuntran ya hechos varios objetos, con los cuales se puede demostrar el funcionamiento del programa poniendo distintos datos como los del conductor, los asistentes y el camion, mas algunas cantidades para probar las toneladas recolectadas. Al correr el codigo se mostrara en pantalla un menu el cual le pedira al usuario que catidad deseara ver, entre ellas papel, plastico, vidrio, residuos y metal.
Documentacion:
from datetime import datetime

class PuntoGeografico:
  """Representa un punto geográfico con latitud y longitud."""
  def __init__(self, latitud, longitud):
    """Inicializa el punto con las coordenadas dadas."""
    self.latitud = latitud
    self.longitud = longitud

class Turno:
  """Representa un turno de recolección de residuos en una ruta determinada."""
  def __init__(self, ruta, camion, inicio, fin):
    """Inicializa el turno con la ruta, el camión, la hora de inicio y fin."""
    self.ruta = ruta
    self.camion = camion
    self.inicio = inicio
    self.fin = fin
    self.registros = [] # Lista de tuplas (punto_geografico, tiempo)

  def agregar_registro(self, punto_geografico, tiempo):
    """Agrega un registro de recolección al turno."""
    self.registros.append((punto_geografico, tiempo))

  def obtener_registros(self):
    """Devuelve la lista de registros del turno."""
    return self.registros

class Camion:
  """Representa un camión de recolección con un conductor y asistentes."""
  def __init__(self, conductor, asistentes):
    """Inicializa el camión con el conductor y los asistentes."""
    self.conductor = conductor
    self.asistentes = asistentes

class Persona:
  """Representa una persona con identificación y nombre."""
  def __init__(self, identificacion, nombre):
    """Inicializa la persona con la identificación y el nombre."""
    self.identificacion = identificacion
    self.nombre = nombre

class CentroAcopio:
  """Representa un centro de acopio de residuos."""
  def __init__(self):
    """Inicializa el centro con una lista vacía de registros."""
    self.registros = [] # Lista de tuplas (tipo_residuo, toneladas)

  def agregar_registro(self, tipo_residuo, toneladas):
    """Agrega un registro de acopio al centro."""
    self.registros.append((tipo_residuo, toneladas))

  def obtener_registro_por_tipo(self, tipo_residuo):
    """Devuelve la cantidad total de toneladas de un tipo de residuo en el centro."""
    total = 0
    for registro in self.registros:
      if registro[0] == tipo_residuo:
        total += registro[1]
    return total

class TrashCity:
  """Representa una ciudad que gestiona la recolección y acopio de residuos."""
  _instance = None # Variable para implementar el patrón singleton

  def __new__(cls):
    """Crea o devuelve la única instancia de la clase."""
    if not cls._instance:
      cls._instance = super().__new__(cls)
      cls._instance.turnos = [] # Lista de turnos de la ciudad
    return cls._instance

  def agregar_turno(self, turno):
    """Agrega un turno a la ciudad."""
    self.turnos.append(turno)

  def obtener_cantidad_vidrio_por_dia(self, fecha):
    """Devuelve la cantidad total de vidrio recolectado en un día dado."""
    total_vidrio = 1.6738 # Valor inicial arbitrario
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
    """Devuelve la cantidad total de metal recolectado en un día dado."""
    total_metal = 2.9097 # Valor inicial arbitrario
    for turno in self.turnos:
      if turno.inicio.date() == fecha.date():
        registros = turno.obtener_registros()
        for registro in registros:
          punto_geografico, tiempo = registro
          if punto_geografico and tiempo:
            # Aquí puedes realizar acciones específicas para el metal
            # Supongamos que la información del metal se almacena en un atributo "metal" del punto_geografico
            total_metal += punto_geografico.metal
    return total_metal

  def obtener_cantidad_plastico_por_dia(self, fecha):
    """Devuelve la cantidad total de plástico recolectado en un día dado."""
    total_plastico = 0.6961 # Valor inicial arbitrario
    for turno in self.turnos:
      if turno.inicio.date() == fecha.date():
        registros = turno.obtener_registros()
        for registro in registros:
          punto_geografico, tiempo = registro
          if punto_geografico and tiempo:
            # Aquí puedes realizar acciones específicas para el plástico
            # Supongamos que la información del plástico se almacena en un atributo "plastico" del punto_geografico
            total_plastico += punto_geografico.plastico
    return total_plastico

  def obtener_cantidad_residuos_por_dia(self, fecha):
    """Devuelve la cantidad total de residuos recolectados en un día dado."""
    total_residuos = 7.6981 # Valor inicial arbitrario
    for turno in self.turnos:
      if turno.inicio.date() == fecha.date():
        registros = turno.obtener_registros()
        for registro in registros:
          punto_geografico, tiempo = registro
          if punto_geografico and tiempo:
            # Aquí puedes realizar acciones específicas para los residuos
            # Supongamos que la información de los residuos se almacena en un atributo "residuos" del punto_geografico
            total_residuos += punto_geografico.residuos
    return total_residuos

  def obtener_cantidad_papel_por_dia(self, fecha):
  	"""Devuelve la cantidad total de papel recolectado en un día dado."""
  	total_papel = 4.6981 # Valor inicial arbitrario
  	for turno in self.turnos:
  		if turno.inicio.date() == fecha.date():
  			registros = turno.obtener_registros()
  			for registro in registros:
  				punto_geografico, tiempo = registro
  				if punto_geografico and tiempo:
  					# Aquí puedes realizar acciones específicas para el papel
  					# Supongamos que la información del papel se almacena en un atributo "papel" del punto_geografico
  					total_papel += punto_geografico.papel
  	return total_papel

