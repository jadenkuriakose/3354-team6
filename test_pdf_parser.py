import pytest

from pdf_parser import extractTextFromPdf


def test_valid_pdf():
    text = extractTextFromPdf("sample.pdf")

    assert text is not None
    assert len(text) > 0


def test_invalid_path():
    with pytest.raises(FileNotFoundError):
        extractTextFromPdf("fake_file.pdf")


def test_empty_path():
    with pytest.raises(ValueError):
        extractTextFromPdf("")
