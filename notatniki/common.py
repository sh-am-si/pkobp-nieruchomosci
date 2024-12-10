from pathlib import Path


def dataDirectory(dataDirectoryName='dane'):
    """
    Zwraca katalog zawierający dane.
    
    Zakładamy, że folder z danymi znajduje się w katalogu nadrzędnym tego pliku i nosi nazwę 'dane'.
    W przypadku innej konfiguracji należy zmodyfikować tę metodę.
    """
    dataDir = Path(__file__).resolve().parent
    while not list(dataDir.rglob('dane')):
        dataDir = dataDir.parent
    found = [d for d in dataDir.rglob('dane') if d.is_dir()]
    if not found:
        raise Exception(f'Nie można znaleźć katalogu {dataDirectoryName} na ścieżce plików źródłowych.')
    return found[0]
    
    
    