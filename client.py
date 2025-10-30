import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print("Lista inicial:", conn.root.exposed_value())
  
  # Append
  conn.root.exposed_append(5)
  conn.root.exposed_append(6)
  conn.root.exposed_append(3)
  conn.root.exposed_append(8)
  print("Após append(5, 6, 3, 8):", conn.root.exposed_value())
  
  # Pesquisa
  print("Busca por 6:", conn.root.exposed_search(6))
  print("Busca por 10:", conn.root.exposed_search(10))
  
  # Insert
  conn.root.exposed_insert(2, 99)
  print("Após insert(2, 99):", conn.root.exposed_value())
  
  # Sort
  conn.root.exposed_sort()
  print("Após sort():", conn.root.exposed_value())
  
  # Reverse
  conn.root.exposed_reverse()
  print("Após reverse():", conn.root.exposed_value())
  
  # Remove
  success, lista = conn.root.exposed_remove(99)
  print("Após remove(99):", lista, "- Sucesso:", success)
  
  # Pop
  success, valor = conn.root.exposed_pop()
  print("Após pop():", valor, "- Lista:", conn.root.exposed_value())
  
  # Clear
  conn.root.exposed_clear()
  print("Após clear():", conn.root.exposed_value())
