from PyPDF2 import PdfReader


def extractTextFromPdf(filePath):
    if not filePath:
        raise ValueError("file path cannot be empty")

    reader = PdfReader(filePath)
    extractedText = []

    for page in reader.pages:
        pageText = page.extract_text()
        if pageText:
            extractedText.append(pageText)

    return "\n".join(extractedText).strip()
