from django.http import JsonResponse
from django.shortcuts import render

from .aws import upload_to_s3
from .models import Attachment


def index(request):
    attachments = Attachment.objects.all()
    context = {
        "attachments": attachments,
    }
    return render(request, 'index.html', context)


def upload(request):
    files = request.FILES.getlist('file')

    urls = []
    for file in files:
        url = upload_to_s3(file)
        file, _ = Attachment.objects.get_or_create(url=url)
        urls.append({"filename": file.filename, "url": file.signed_url})

    print(urls)
    context = {
        "urls": urls,
    }
    return JsonResponse(context)
