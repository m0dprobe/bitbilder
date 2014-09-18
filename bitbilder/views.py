from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings

from bitbilder.models import Bit
from bitbilder.forms import BitForm, ClaimForm

import io, zipfile, os

# Create your views here.

def matrix(request):
    bit_list = Bit.objects.order_by('bitname')
    context = {'bit_list': bit_list}
    return render(request, 'bitbilder/matrix.html', context)

def details(request, bit_id):
    bit = get_object_or_404(Bit, pk=bit_id)
    return render(request, 'bitbilder/detail.html', {'bit': bit})

def upload(request, param=""):
    svgerr = False
    if param == "svgerr":
        svgerr = True
    else:
        svgerr = False

    if request.method == "POST":
        form = BitForm(request.POST, request.FILES)
        reqpost = request.POST
        reqfiles = request.FILES
        if form.is_valid():
            newbit = Bit(
                bitname = reqpost['bitname'],
                author = reqpost['author'],
                creation_date = reqpost['creation_date'],
                license = reqpost['license'],
                bit_image = reqfiles['bit_image'],
                bit_vector = reqfiles['bit_vector'],
                reserved = reqfiles.get('reserved', False),
                reserved_for = reqfiles.get('reserved_for', "")
            )
            newbit.save()
            return HttpResponseRedirect('/bits/')
        else:
            return HttpResponseRedirect('svgerr')


    form = BitForm()
    return render(request, 'bitbilder/upload.html', {'form': form, 'svg_error': svgerr})

def claim(request, bit_id):
    if request.method == "POST":
        form = ClaimForm(request.POST)
        if form.is_valid():
            b = Bit.objects.get(id=bit_id)
            b.reserved = True
            b.reserved_for = request.POST['claimed_by']
            b.save()

            return HttpResponseRedirect('/bits/%s' % bit_id)
    form = ClaimForm()
    bit = get_object_or_404(Bit, pk=bit_id)
    return render(request, 'bitbilder/claim.html', {'form': form, 'bit': bit})

def download_svg_zip(request):
    files = []
    for bit in Bit.objects.all():
        files.append(bit.bit_vector.path)

    zip_subdir = "all_bits_svg"
    zip_filename = "%s.zip" % zip_subdir

    s = io.BytesIO()
    zf = zipfile.ZipFile(s, "w")

    for fpath in files:
        f = open(fpath, "rb")
        fcon = f.read()
        fdir, fname = os.path.split(fpath)
        zf.writestr(fname, fcon)

    zf.close()

    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp

def download_img_zip(request):
    files = []
    for bit in Bit.objects.all():
        files.append(bit.bit_image.path)

    zip_subdir = "all_bits_img"
    zip_filename = "%s.zip" % zip_subdir

    s = io.BytesIO()
    zf = zipfile.ZipFile(s, "w")

    for fpath in files:
        f = open(fpath, "rb")
        fcon = f.read()
        fdir, fname = os.path.split(fpath)
        zf.writestr(fname, fcon)

    zf.close()

    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp

def download_page(request):
    return render(request, 'bitbilder/download.html', {})
