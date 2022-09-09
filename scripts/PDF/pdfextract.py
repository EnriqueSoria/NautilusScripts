#!/usr/bin/env fades
from pathlib import Path

from PyPDF2 import PdfReader, PdfMerger  # fades PyPDF2


def split_pdf_files(filename: str):
    num_pages = len(PdfReader(filename).pages)

    file_path = Path(filename)

    for page in range(num_pages):
        page_filename = file_path.parent / f"splitted-{page}-{file_path.name}"

        merger = PdfMerger()
        merger.append(filename, pages=(page, page + 1))

        with open(page_filename, "wb") as page_file:
            merger.write(page_file)


if __name__ == "__main__":
    from os import getenv

    for filename in getenv("NAUTILUS_SCRIPT_SELECTED_FILE_PATHS", "").splitlines():
        if filename:
            split_pdf_files(filename)
