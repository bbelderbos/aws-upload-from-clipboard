from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .aws import upload_to_s3
from .models import Attachment


def index(request):
    attachments = Attachment.objects.all()
    context = {
        "attachments": attachments,
    }
    return render(request, 'index.html', context)


@require_POST
def upload(request):
    files = request.FILES.getlist('file')

    urls = []
    for file in files:
        url = upload_to_s3(file)
        file, _ = Attachment.objects.get_or_create(url=url)
        urls.append({"filename": file.filename, "url": file.signed_url})

    context = {
        "urls": urls,
    }
    return JsonResponse(context)
