def correl(a,b):
  # average a
  sum_a = 0
  av_a = 0
  for elem in a:
    sum_a += elem
  av_a = sum_a / len(a)
  
  # average b
  sum_b = 0
  av_b = 0
  for elem in b:
    sum_b += elem
    av_b = sum_b / len(b)
  
  # average sigma_a
  sum_sa = 0
  for elem in a:
    sum_sa += (elem - av_a) ** 2
  sigma_a = (sum_sa/len(a)) ** 0.5
  
  # average sigma_b
  sum_sb = 0
  for elem in b:
    sum_sb += (elem - av_b) ** 2
  sigma_b = (sum_sb / len(b)) ** 0.5
  
  # correl
  sum_ab = 0
  for i in range(len(a)):
    sum_ab += (a[i] - av_a)*(b[i] - av_b)
    
  correl = (sum_ab / len(a)) / (sigma_a * sigma_b)
  
  return correl
    
  
