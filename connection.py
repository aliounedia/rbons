import pyodbc
import settings
def get_connection():
    ''' connexion a la base de donnees  '''
    try:
        return pyodbc.connect(
           getattr(settings,
                   "CONNEXION_STRING"),
                   autocommit =True)
    except:
        raise  Exception(
    'Erreur ce connection reseau, sans dourte!')
