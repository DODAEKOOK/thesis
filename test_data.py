from PSD.models import PSD

fa=open('PSDdata/alpha_PSD_af_value_KJH_12_ecd.txt','r')

eegpsda = [] 

while True:
     testline = fa.readline()
     if len(testline) == 0:
      break #EOF
     testline = testline.split()
     eegpsda.append([])
     for i in range(0,1):
      eegpsda[-1].append(float(testline[i])) 

k = []

for i in range(21):
     t = eegpsda[i]
     k.append(t[0])

for i in range(21):
     PSD.objects.create(PSD_value=k[i])
