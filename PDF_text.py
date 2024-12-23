import PyPDF2

def pdf_to_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_text = pdf_to_text('AutomationKT.pdf')

with open('out_put.txt', 'w', encoding='utf-8') as file:
    file.write(pdf_text)

print("PDF content has been written to out_put.txt.")
