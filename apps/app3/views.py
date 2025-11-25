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
    upload_info = None  # <-- For showing only the latest upload

    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        file_name = uploaded_file.name
        file_size = uploaded_file.size

        try:
            # Save file
            fs = FileSystemStorage()
            saved_path = fs.save(uploaded_file.name, uploaded_file)
            full_path = fs.path(saved_path)
            file_url = fs.url(saved_path)

            # Initialize defaults
            page_count = None
            paper_size = None

            # --- PROCESS PDF ---
            if file_name.lower().endswith(".pdf"):
                with open(full_path, "rb") as pdf:
                    reader = PyPDF2.PdfReader(pdf)
                    page_count = len(reader.pages)
                    paper_size = detect_pdf_paper_size(reader)

            # --- PROCESS DOCX ---
            elif file_name.lower().endswith(".docx"):
                document = Document(full_path)
                text = " ".join([p.text for p in document.paragraphs])
                words = len(text.split())
                page_count = max(1, words // 300 + 1)
                paper_size = detect_docx_paper_size(document)

            else:
                error = "Unsupported file type."

            # Save to DB only if no error
            if error is None:
                UploadedDocument.objects.create(
                    user=request.user,
                    file=saved_path,
                    filename=file_name,
                    page_count=page_count,
                    file_size=file_size,
                    paper_size=paper_size,
                )

                # Data to display immediately
                upload_info = {
                    "filename": file_name,
                    "file_url": file_url,
                    "page_count": page_count,
                    "paper_size": paper_size,
                    "file_size": file_size,
                }

        except Exception as e:
            error = f"Error: {e}"

    # ALWAYS load all documents
    documents = UploadedDocument.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    return render(request, "app3/index.html", {
        "upload_info": upload_info,  # newest uploaded file summary
        "documents": documents,  # list of all uploaded files
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

def print_document(request, doc_id):
    try:
        doc = UploadedDocument.objects.get(id=doc_id, user=request.user)
    except UploadedDocument.DoesNotExist:
        return HttpResponse("Document not found.", status=404)

    file_path = doc.file.path

    # Windows printing sample (prints default printer)
    try:
        os.startfile(file_path, "print")
        return HttpResponse("Printing sent to printer.")
    except Exception as e:
        return HttpResponse(f"Print error: {e}", status=500)
