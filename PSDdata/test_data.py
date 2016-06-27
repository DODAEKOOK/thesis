from PSD.models import PSD

NM = 'PSH' #LKJ, KJH, LMW, PSH
cycles = '18' #12, 14, 16, 18
tm = 'af' #af,be

mark = 'S4a18'
svg_val = '4.8' #14.12 / 6.72 / 6.72 / 4.8 (12, 25, 25, 35)

# S1b12, S1b14, S1b16, S1b18
# S1a12, S1a14, S1a16, S1a18

# S2b12, S2b14, S2b16, S2b18
# S2a12, S2a14, S2a16, S2a18

# S3b12, S3b14, S3b16, S3b18
# S3a12, S3a14, S3a16, S3a18

# S4b12, S4b14, S4b16, S4b18
# S4a12, S4a14, S4a16, S4a18

#############################################

fa=open('PSDdata/freq_svg.txt','r') #PSDdata/

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
k_svg = []


fb=open('PSDdata/alpha_PSD_%s_value_%s_%s_ecd.txt' % (tm, NM, cycles),'r')

eegpsdb = [] 

while True:
     testline = fb.readline()
     if len(testline) == 0:
      break #EOF
     testline = testline.split()
     eegpsdb.append([])
     for i in range(0,1):
          eegpsdb[-1].append(float(testline[i])) 

j = []
j_svg = []

for i in range(21):
     t = eegpsda[i]
     k_svg.append(t[0])
     k.append(8+i*float(0.246952380952381))
     t = eegpsdb[i]
     j.append(t[0])
     j_svg.append(float(229.76881607009867) - (t[0] * (10**12) * float(svg_val)))


for i in range(21):
     PSD.objects.create(PSD_value=j[i],Freq_value=k[i],PSD_svg=j_svg[i],Freq_svg=k_svg[i],sc_tag='%s'%(mark))

