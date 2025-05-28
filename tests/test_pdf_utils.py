import os
import tempfile
import shutil
import pytest
from pathlib import Path
from PyPDF2 import PdfWriter
from pdf_password_remover.utils import pdf_utils

TEST_PASSWORD = "testpass"

@pytest.fixture
def temp_pdf(tmp_path):
    pdf_path = tmp_path / "protected.pdf"
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with open(pdf_path, "wb") as f:
        writer.encrypt(TEST_PASSWORD)
        writer.write(f)
    return pdf_path

@pytest.fixture
def temp_dir_with_pdfs(tmp_path):
    dir_path = tmp_path / "pdfs"
    dir_path.mkdir()
    pdfs = []
    for i in range(3):
        pdf_path = dir_path / f"file_{i}.pdf"
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with open(pdf_path, "wb") as f:
            writer.encrypt(TEST_PASSWORD)
            writer.write(f)
        pdfs.append(pdf_path)
    return dir_path, pdfs

def test_remove_password_single_pdf(temp_pdf, tmp_path):
    output_dir = tmp_path / "out"
    output_dir.mkdir()
    out_files = pdf_utils.PDFPasswordRemover.remove_password(
        str(temp_pdf), TEST_PASSWORD, str(output_dir)
    )
    assert len(out_files) == 1
    assert Path(out_files[0]).exists()

def test_remove_password_wrong_password(temp_pdf, tmp_path):
    import click
    output_dir = tmp_path / "out"
    output_dir.mkdir()
    with pytest.raises(click.exceptions.Exit):
        pdf_utils.PDFPasswordRemover.remove_password(
            str(temp_pdf), "wrongpass", str(output_dir)
        )

def test_remove_password_directory(temp_dir_with_pdfs, tmp_path):
    dir_path, pdfs = temp_dir_with_pdfs
    output_dir = tmp_path / "out"
    output_dir.mkdir()
    out_files = pdf_utils.PDFPasswordRemover.remove_password(
        str(dir_path), TEST_PASSWORD, str(output_dir)
    )
    assert len(out_files) == len(pdfs)
    for out_file in out_files:
        assert Path(out_file).exists()

def test_remove_password_file_not_found(tmp_path):
    import click
    fake_path = tmp_path / "doesnotexist.pdf"
    with pytest.raises(click.exceptions.Exit):
        pdf_utils.PDFPasswordRemover.remove_password(
            str(fake_path), TEST_PASSWORD
        )

