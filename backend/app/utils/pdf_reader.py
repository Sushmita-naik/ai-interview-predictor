import fitz  # PyMuPDF


def read_pdf(pdf_path):
    """
    Extract text from a PDF file
    """

    try:
        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    except Exception as e:

        print(
            f"Error reading PDF: {e}"
        )

        return ""


def get_pdf_page_count(pdf_path):
    """
    Return total number of pages
    """

    try:
        document = fitz.open(pdf_path)

        page_count = len(document)

        document.close()

        return page_count

    except Exception as e:

        print(
            f"Error counting pages: {e}"
        )

        return 0


def get_pdf_metadata(pdf_path):
    """
    Extract PDF metadata
    """

    try:
        document = fitz.open(pdf_path)

        metadata = document.metadata

        document.close()

        return metadata

    except Exception as e:

        print(
            f"Error reading metadata: {e}"
        )

        return {}


def validate_pdf(pdf_path):
    """
    Check if PDF is valid
    """

    try:
        document = fitz.open(pdf_path)

        document.close()

        return True

    except Exception:

        return False


if __name__ == "__main__":

    pdf_file = "uploads/resumes/sample_resume.pdf"

    print(
        "Valid PDF:",
        validate_pdf(pdf_file)
    )

    print(
        "Page Count:",
        get_pdf_page_count(pdf_file)
    )

    print(
        "Metadata:",
        get_pdf_metadata(pdf_file)
    )

    print(
        "\nExtracted Text:\n"
    )

    print(
        read_pdf(pdf_file)
    )