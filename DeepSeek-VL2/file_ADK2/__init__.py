# check if python version is above 3.10
import sys

if sys.version_info >= (3, 10):
    print("Python version is above 3.10, patching the collections module.")
    # Monkey patch collections
    import collections
    import collections.abc

    for type_name in collections.abc.__all__:
        setattr(collections, type_name, getattr(collections.abc, type_name))


  # !ATTENZIONE !
  # DAL 9 MAGGIO DEL 2025 IN POI, I KERNEL LINUX NON SARANNO PIù COMPATIVBILI CON 
  # I MIE PROGRAMMI, UTILIZZARE AL MASSIMO UN WSL2/WSL1 O UNA VMware
  # problemi:
  # 1. troppo difficle
  # 2. lentezza
  # 3. mi sta sul cazzo aspettare il consenso.
  # KONATA - 2025
  
