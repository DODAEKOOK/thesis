from django.shortcuts import render
from .models import PSD

# Create your views here.

#LKJ, KJH, LMW, PSH

# S1b12, S1b14, S1b16, S1b18
# S1a12, S1a14, S1a16, S1a18

# S2b12, S2b14, S2b16, S2b18
# S2a12, S2a14, S2a16, S2a18

# S3b12, S3b14, S3b16, S3b18
# S3a12, S3a14, S3a16, S3a18

# S4b12, S4b14, S4b16, S4b18
# S4a12, S4a14, S4a16, S4a18

def sub_intro(request):
    """

    a = PSD.objects.all()[:5]
    print(a) --> [(PSD:PSD object),() ... ]
    print(a[0].PSD_value) --> 3.44e-12

    aa = PSD.objects.all()
    s1b12_data = aa[0].PSD_value

    """
    return render(request, 'PSD/psd_intro.html', {})

def sub1(request):
    psds1b12 = PSD.objects.all().filter(sc_tag='S1b12')
    psds1a12 = PSD.objects.all().filter(sc_tag='S1a12')
    psds1b14 = PSD.objects.all().filter(sc_tag='S1b14')
    psds1a14 = PSD.objects.all().filter(sc_tag='S1a14')
    psds1b16 = PSD.objects.all().filter(sc_tag='S1b16')
    psds1a16 = PSD.objects.all().filter(sc_tag='S1a16')
    psds1b18 = PSD.objects.all().filter(sc_tag='S1b18')
    psds1a18 = PSD.objects.all().filter(sc_tag='S1a18')

    psds1b12_avr = mk_avr(psds1b12)
    psds1a12_avr = mk_avr(psds1a12)
    psds1b14_avr = mk_avr(psds1b14)
    psds1a14_avr = mk_avr(psds1a14)
    psds1b16_avr = mk_avr(psds1b16)
    psds1a16_avr = mk_avr(psds1a16)
    psds1b18_avr = mk_avr(psds1b18)
    psds1a18_avr = mk_avr(psds1a18)

    return render(request, 'PSD/sub1.html', {'psds1b12': psds1b12, 'psds1a12': psds1a12,
                                            'psds1b14': psds1b14, 'psds1a14': psds1a14,
                                            'psds1b16': psds1b16, 'psds1a16': psds1a16,
                                            'psds1b18': psds1b18, 'psds1a18': psds1a18,
                                             'psds1b12_avr': psds1b12_avr,
                                             'psds1a12_avr': psds1a12_avr,
                                             'psds1b14_avr': psds1b14_avr,
                                             'psds1a14_avr': psds1a14_avr,
                                             'psds1b16_avr': psds1b16_avr,
                                             'psds1a16_avr': psds1a16_avr,
                                             'psds1b18_avr': psds1b18_avr,
                                             'psds1a18_avr': psds1a18_avr})

def sub2(request):
    psds2b12 = PSD.objects.all().filter(sc_tag='S2b12')
    psds2a12 = PSD.objects.all().filter(sc_tag='S2a12')
    psds2b14 = PSD.objects.all().filter(sc_tag='S2b14')
    psds2a14 = PSD.objects.all().filter(sc_tag='S2a14')
    psds2b16 = PSD.objects.all().filter(sc_tag='S2b16')
    psds2a16 = PSD.objects.all().filter(sc_tag='S2a16')
    psds2b18 = PSD.objects.all().filter(sc_tag='S2b18')
    psds2a18 = PSD.objects.all().filter(sc_tag='S2a18')

    psds2b12_avr = mk_avr(psds2b12)
    psds2a12_avr = mk_avr(psds2a12)
    psds2b14_avr = mk_avr(psds2b14)
    psds2a14_avr = mk_avr(psds2a14)
    psds2b16_avr = mk_avr(psds2b16)
    psds2a16_avr = mk_avr(psds2a16)
    psds2b18_avr = mk_avr(psds2b18)
    psds2a18_avr = mk_avr(psds2a18)

    return render(request, 'PSD/sub2.html', {'psds2b12': psds2b12, 'psds2a12': psds2a12,
                                            'psds2b14': psds2b14, 'psds2a14': psds2a14,
                                            'psds2b16': psds2b16, 'psds2a16': psds2a16,
                                            'psds2b18': psds2b18, 'psds2a18': psds2a18,
                                             'psds2b12_avr': psds2b12_avr,
                                             'psds2a12_avr': psds2a12_avr,
                                             'psds2b14_avr': psds2b14_avr,
                                             'psds2a14_avr': psds2a14_avr,
                                             'psds2b16_avr': psds2b16_avr,
                                             'psds2a16_avr': psds2a16_avr,
                                             'psds2b18_avr': psds2b18_avr,
                                             'psds2a18_avr': psds2a18_avr})

def sub3(request):
    psds3b12 = PSD.objects.all().filter(sc_tag='S3b12')
    psds3a12 = PSD.objects.all().filter(sc_tag='S3a12')
    psds3b14 = PSD.objects.all().filter(sc_tag='S3b14')
    psds3a14 = PSD.objects.all().filter(sc_tag='S3a14')
    psds3b16 = PSD.objects.all().filter(sc_tag='S3b16')
    psds3a16 = PSD.objects.all().filter(sc_tag='S3a16')
    psds3b18 = PSD.objects.all().filter(sc_tag='S3b18')
    psds3a18 = PSD.objects.all().filter(sc_tag='S3a18')

    psds3b12_avr = mk_avr(psds3b12)
    psds3a12_avr = mk_avr(psds3a12)
    psds3b14_avr = mk_avr(psds3b14)
    psds3a14_avr = mk_avr(psds3a14)
    psds3b16_avr = mk_avr(psds3b16)
    psds3a16_avr = mk_avr(psds3a16)
    psds3b18_avr = mk_avr(psds3b18)
    psds3a18_avr = mk_avr(psds3a18)

    return render(request, 'PSD/sub3.html', {'psds3b12': psds3b12, 'psds3a12': psds3a12,
                                            'psds3b14': psds3b14, 'psds3a14': psds3a14,
                                            'psds3b16': psds3b16, 'psds3a16': psds3a16,
                                            'psds3b18': psds3b18, 'psds3a18': psds3a18,
                                             'psds3b12_avr': psds3b12_avr,
                                             'psds3a12_avr': psds3a12_avr,
                                             'psds3b14_avr': psds3b14_avr,
                                             'psds3a14_avr': psds3a14_avr,
                                             'psds3b16_avr': psds3b16_avr,
                                             'psds3a16_avr': psds3a16_avr,
                                             'psds3b18_avr': psds3b18_avr,
                                             'psds3a18_avr': psds3a18_avr})

def sub4(request):
    psds4b12 = PSD.objects.all().filter(sc_tag='S4b12')
    psds4a12 = PSD.objects.all().filter(sc_tag='S4a12')
    psds4b14 = PSD.objects.all().filter(sc_tag='S4b14')
    psds4a14 = PSD.objects.all().filter(sc_tag='S4a14')
    psds4b16 = PSD.objects.all().filter(sc_tag='S4b16')
    psds4a16 = PSD.objects.all().filter(sc_tag='S4a16')
    psds4b18 = PSD.objects.all().filter(sc_tag='S4b18')
    psds4a18 = PSD.objects.all().filter(sc_tag='S4a18')

    psds4b12_avr = mk_avr(psds4b12)
    psds4a12_avr = mk_avr(psds4a12)
    psds4b14_avr = mk_avr(psds4b14)
    psds4a14_avr = mk_avr(psds4a14)
    psds4b16_avr = mk_avr(psds4b16)
    psds4a16_avr = mk_avr(psds4a16)
    psds4b18_avr = mk_avr(psds4b18)
    psds4a18_avr = mk_avr(psds4a18)

    return render(request, 'PSD/sub4.html', {'psds4b12': psds4b12, 'psds4a12': psds4a12,
                                            'psds4b14': psds4b14, 'psds4a14': psds4a14,
                                            'psds4b16': psds4b16, 'psds4a16': psds4a16,
                                            'psds4b18': psds4b18, 'psds4a18': psds4a18,
                                             'psds4b12_avr': psds4b12_avr,
                                             'psds4a12_avr': psds4a12_avr,
                                             'psds4b14_avr': psds4b14_avr,
                                             'psds4a14_avr': psds4a14_avr,
                                             'psds4b16_avr': psds4b16_avr,
                                             'psds4a16_avr': psds4a16_avr,
                                             'psds4b18_avr': psds4b18_avr,
                                             'psds4a18_avr': psds4a18_avr})

def mk_avr(v):
    avr_list = []
    for i in v:
        avr_list.append(i.PSD_value)
    avr_v = sum(avr_list) / len(avr_list)
    return avr_v