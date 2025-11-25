from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from docx import Document
import PyPDF2
from .models import UploadedDocument
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from docx import Document
import PyPDF2
from .models import UploadedDocument

def index(request):
    error = None
    upload_info = None  # latest upload

    # Price per page in PHP
    price_map = {
        "Long": 5,
        "Short": 3,
        "A4": 4,
        # default price for custom sizes
        "Custom": 6
    }

    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        file_name = uploaded_file.name
        file_size = uploaded_file.size

        try:
            fs = FileSystemStorage()
            saved_path = fs.save(uploaded_file.name, uploaded_file)
            full_path = fs.path(saved_path)
            file_url = fs.url(saved_path)

            # Defaults
            page_count = None
            paper_size = None

            # Process PDF
            if file_name.lower().endswith(".pdf"):
                with open(full_path, "rb") as pdf:
                    reader = PyPDF2.PdfReader(pdf)
                    page_count = len(reader.pages)
                    paper_size = detect_pdf_paper_size(reader)

            # Process DOCX
            elif file_name.lower().endswith(".docx"):
                document = Document(full_path)
                text = " ".join([p.text for p in document.paragraphs])
                words = len(text.split())
                page_count = max(1, words // 300 + 1)
                paper_size = detect_docx_paper_size(document)

            else:
                error = "Unsupported file type."

            if error is None:
                UploadedDocument.objects.create(
                    user=request.user,
                    file=saved_path,
                    filename=file_name,
                    page_count=page_count,
                    file_size=file_size,
                    paper_size=paper_size,
                )

                # Determine price per page
                key = paper_size if paper_size in price_map else "Custom"
                total_amount = page_count * price_map[key]

                upload_info = {
                    "filename": file_name,
                    "file_url": file_url,
                    "page_count": page_count,
                    "paper_size": paper_size,
                    "file_size": file_size,
                    "total_amount": total_amount,
                }

        except Exception as e:
            error = f"Error: {e}"

    documents = UploadedDocument.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    # Add total_amount for each document
    for doc in documents:
        key = doc.paper_size if doc.paper_size in price_map else "Custom"
        doc.total_amount = doc.page_count * price_map[key]

    return render(request, "app3/index.html", {
        "upload_info": upload_info,
        "documents": documents,
        "error": error,
    })



def detect_pdf_paper_size(reader):
    page = reader.pages[0]
    media_box = page.mediabox
    
    width_pt = float(media_box.width)
    height_pt = float(media_box.height)

    mm_width = width_pt * 0.352777
    mm_height = height_pt * 0.352777

    sizes = {
        "A4": (210, 297),
        "Letter": (216, 279),
        "Legal": (216, 356),
    }

    for name, (w, h) in sizes.items():
        if abs(mm_width - w) < 5 and abs(mm_height - h) < 5 or \
           abs(mm_width - h) < 5 and abs(mm_height - w) < 5:
            return name

    return f"Custom ({round(mm_width)}mm x {round(mm_height)}mm)"
# apps/app3/views.py

import os
import subprocess
from django.http import HttpResponse
from .models import UploadedDocument
import win32print
import win32api

def print_document(request, doc_id):
    doc = UploadedDocument.objects.get(id=doc_id, user=request.user)
    file_path = doc.file.path

    try:
        printer_name = win32print.GetDefaultPrinter()
        win32api.ShellExecute(0, "print", file_path, f'/d:"{printer_name}"', ".", 0)
        return HttpResponse("Printing sent to printer.")
    except Exception as e:
        return HttpResponse(f"Print error: {e}", status=500)