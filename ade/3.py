def pangkat(bilangan,pangkat):
  if (bilangan < 0):
    return print("Hanya Masukkan bilangan positif")
  elif (type(bilangan) != int):
    return print("Hanya Masukkan bilangan bulat")

  return (bilangan**pangkat)
  
pangkat(3,2)