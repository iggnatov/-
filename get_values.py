import data as dl

# Обработка значений отметок по информатике
def info_marks():
  datamarks = dl.info_marks.split('\n') 
  info_marks = []
  for elem in datamarks:
    if elem:
      st = elem.split()
      for s in st:
        s = s.replace(',','.')
        s = float(s)
        info_marks.append(s)
  return info_marks

# Обработка значений отметок по английскому языку
def english_marks():
  datamarks = dl.english_marks.split('\n') 
  engmarks = []
  for elem in datamarks:
    if elem:
      st = elem.split()
      for s in st:
        s = s.replace(',','.')
        s = float(s)
        engmarks.append(s)
  return engmarks
  
# Обработка значений данных средней продолжительности времени сна
def sleep_time():
  datasleep = dl.sleep_time.split('\n') 
  sleeptime = []
  for elem in datasleep:
    if elem:
      st = elem.split()
      for s in st:
        s = s.replace(',','.')
        s = float(s)
        sleeptime.append(s)
  return sleeptime

# Обработка значений отметок по математике  
def math_marks():
  datamarks = dl.math_marks.split('\n')
  mathmarks = []
  for elem in datamarks:
    if elem:
      mm = elem.split()
      for m in mm:
        m = m.replace(',','.')
        m = float(m)
        mathmarks.append(m)
  return mathmarks

# Обработка значений отметок по русскому языку
def russ_marks():
  datamarks = dl.russ_marks.split('\n')
  russmarks = []
  for elem in datamarks:
    if elem:
      rm = elem.split()
      for r in rm:
        r = r.replace(',','.')
        r = float(r)
        russmarks.append(r)
  return russmarks

# Обработка значений данных о наличии домашнего животного 
def having_pet():
  datapet = dl.having_pet.split('\n')
  pets = []
  for elem in datapet:
    if elem:
      pp = elem.split()
      for p in pp:
        p = float(p)
        pets.append(p)
  return pets

# Обработка значений данных наличии собственного компьютера
def having_computer():
  datacomp = dl.having_computer.split('\n')
  comps = []
  for elem in datacomp:
    if elem:
      cc = elem.split()
      for c in cc:
        c = float(c)
        comps.append(c)
  return comps

# Обработка значений данных занятиях спортом
def sport():
  datasport = dl.sport.split('\n')
  sport = []
  for elem in datasport:
    if elem:
      ss = elem.split()
      for s in ss:
        s = float(s)
        sport.append(s)
  return sport

# Обработка значений данных о чтении
def reading():
  dataread = dl.reading.split('\n')
  read = []
  for elem in dataread:
    if elem:
      rr = elem.split()
      for r in rr:
        r = float(r)
        read.append(r)
  return read

# Обработка значений данных о наличии отдельной комнаты
def room():
  dataroom = dl.room.split('\n')
  rooms = []
  for elem in dataroom:
    if elem:
      rr = elem.split()
      for r in rr:
        r = float(r)
        rooms.append(r)
  return rooms

# Обработка значений данных о наличии Хобби
def hobby():
  datahobby = dl.hobby.split('\n')
  hobby = []
  for elem in datahobby:
    if elem:
      hh = elem.split()
      for h in hh:
        h = float(h)
        hobby.append(h)
  return hobby

# Обработка значений моего фактора 1  
def my1():
  data1 = dl.my1.split('\n') 
  my = []
  for elem in data1:
    if elem:
      mm = elem.split()
      for m in mm:
        m = m.replace(',','.')
        m = float(m)
        my.append(m)
  return my

# Обработка значений моего фактора 2
def my2():
  data2 = dl.my2.split('\n') 
  my = []
  for elem in data2:
    if elem:
      mm = elem.split()
      for m in mm:
        m = m.replace(',','.')
        m = float(m)
        my.append(m)
  return my
