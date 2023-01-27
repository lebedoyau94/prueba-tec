#Librerias necesarias
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import conexionBD as conexionBD

#Clase tipo vacante
class Vacante:
  def __init__(self, titulo, empresa, ciudad):
    self.titulo = titulo
    self.empresa = empresa
    self.ciudad = ciudad

#Obtenemos el html de la web de vacantes de empleo

url = 'https://www.elempleo.com/co/ofertas-empleo/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
vacantes = soup.find_all(class_="result-item")

#Extraemos todos los datos de cada vacante y los guardamos en una lista
def extraer_vacantes():
  job_list = []
  for vacante in vacantes:
    titulo = vacante.find('a', class_="text-ellipsis js-offer-title")
    empresa = vacante.find('span', class_='info-company-name js-offer-company')
    ciudad = vacante.find('span', class_='info-city js-offer-city')

    job_list.append(Vacante(titulo.text.strip(), empresa.text.strip(), ciudad.text.strip()))
  return job_list

#Definimos la las paginas que existen para hacer la paginacion
def pagina_siguiente():
  page = soup.find('ul', class_='pagination')
  if not page.find_all('li', class_='disabled')[-1]:
    print()

#Funcion principal
def main():
  #Extraemos los datos de la web
  lista_vacantes = extraer_vacantes()

  #Establecemos la conexion a la base de datos MySQL
  conexion = conexionBD.Conexion()

  for vacante in lista_vacantes:
    #Insertamos los datos de la vacante en la base de datos mediante una query
    conexion.insertar(vacante.titulo,vacante.empresa,vacante.ciudad)
  
main()
  



