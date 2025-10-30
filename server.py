import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value
  
  def exposed_search(self, data):
    try:
      return self.value.index(data)
    except ValueError:
      return -1
  
  def exposed_remove(self, data):
    try:
      self.value.remove(data)
      return True, self.value
    except ValueError:
      return False, self.value
  
  def exposed_insert(self, index, data):
    self.value.insert(index, data)
    return self.value
  
  def exposed_sort(self, reverse=False):
    self.value.sort(reverse=reverse)
    return self.value
  
  def exposed_clear(self):
    self.value = []
    return self.value
  
  def exposed_reverse(self):
    self.value.reverse()
    return self.value
  
  def exposed_pop(self, index=-1):
    try:
      return True, self.value.pop(index)
    except IndexError:
      return False, None

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

