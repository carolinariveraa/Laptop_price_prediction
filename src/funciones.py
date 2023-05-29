def replace_with_other(df, column, values):
    df[column] = df[column].apply(lambda x: x if x in values else 'Other')
    return df

def inches(s):
    s = str(s)  # Convertir a cadena de texto
    s = float(s.split('"')[0])
    return s

def fetch_processor(x):
  cpu_name = " ".join(x.split()[0:3])
  if cpu_name == 'Intel Core i7' or cpu_name == 'Intel Core i5' or cpu_name == 'Intel Core i3':
    return cpu_name
  elif cpu_name.split()[0] == 'Intel':
    return 'Other Intel Processor'
  else:
    return 'AMD Processor'
  
def gb(s):
    s = str(s)  # Convertir a cadena de texto
    s = float(s.split('GB')[0])
    return s

def storage(d):
    if 'SSD' in d:
        s = 'SSD'
    elif 'HDD' in d:
        s = 'HDD'
    elif 'Flash Storage' in d:
        s = 'Flash Storage'
    elif 'Hybrid' in d:
        s = 'Hybrid'
    elif ('SSD' in d and 'HDD' in d):
        s = 'Hybrid'
    else:
        s = 'Other'
    return s

def weight(s):
    s = str(s)  # Convertir a cadena de texto
    s = float(s.split('kg')[0])
    return s

def cat_os(text):
    if text=='Windows 10' or text=='Windows 7' or text=='Windows 10 S':
        return 'Windows'
    
    elif text=='Mac OS X' or text=='macOS':
        return 'Mac'
    
    else:
        return 'Other'




  
