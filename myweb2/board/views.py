from django.shortcuts import render
from board.models import Board, Comment

def list(request):
    boardCount=Board.objects.count()
    boardList=Board.objects.order_by('-idx')
    print(1)
    return render(request, 'list.html', {'boardList':boardList, 'boardCount':boardCount})

def write(request):
    print(1)
    return render(request, 'write.html')

import os
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
UPLOAD_DIR = 'C:/upload/'

@csrf_exempt
def insert(request):
    print(1)
    fname=''
    print(1)
    fsize=0
    print(2)
    if 'file' in request.FILES:
        print(3)
        file=request.FILES['file']
        print(4)
        fname=file._name
        print(5)
        with open('%s%s' % (UPLOAD_DIR, fname), 'wb') as fp:
            for chunk in file.chunks():
                fp.write(chunk)
        fsize=os.path.getsize(UPLOAD_DIR + fname)
    row=Board(writer=request.POST.get('writer'),
            title=request.POST.get('title'), content=request.POST.get('content'),
            filename=fname, filesize=fsize)
    row.save()
    print(6)
    return redirect('/')

def detail(request):
    print("**")
    id=request.GET.get('idx')
    print(id)
    row=Board.objects.get(idx=id)
    row.hit_up()
    row.save()
    filesize='%.2f' % (row.filesize / 1024)
    print(4)
    return render(request, 'detail.html', {'row':row, 'filesize':filesize})


@csrf_exempt
def update(request):
    print("^^")
    id=request.POST.get('idx')
    print(id)
    row_src=Board.objects.get(idx=id)
    fname=row_src.filename
    fsize=row_src.filesize
    if 'file' in request.FILES:
        file=request.FILES['file']
        fname=file._name
        with open('%s%s' % (UPLOAD_DIR, fname), 'wb') as fp:
            for chunk in file.chunks():
                fp.write(chunk)
        fsize=os.path.getsize(UPLOAD_DIR + fname)

    row_new=Board(idx=id, writer=request.POST.get('writer'),
                  title=request.POST.get('title'), content=request.POST.get('content'),
                  filename=fname, filesize=fsize)
    row_new.save()
    print(5)
    return redirect('/')

def delete(request):
    id=request.POST.get('idx')
    Board.objects.get(idx=id).delete()
    print(6)
    return redirect('/')

from django.utils.http import urlquote
from django.http import HttpResponse, HttpResponseRedirect

def download(request):
    id=request.GET.get('idx')
    row=Board.objects.get(idx=id)
    path=UPLOAD_DIR + row.filename
    filename=os.path.basename(path)
    filename=urlquote(filename)
    with open(path, 'rb') as file:
        response=HttpResponse(file.read(),
                              content_type='application/octet-stream')
        response['Content-Disposition']=\
            "attchment;filename*=UTF-8''{0}".format(filename)
        row.down_up()
        row.save()
        print(7)
        return response

def reply_insert(request):
    id=request.POST.get('idx')
    row=Comment(board_idx=id, writer=request.POST.get('writer'),
                content=request.POST.get('content'))
    print(8)
    return HttpResponseRedirect('detail?idx='+id)