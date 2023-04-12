#!env python3


import os
import sys
import PyPDF2


def split_pdf(input_pdf_path, output_folder):
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])

            output_pdf_path = os.path.join(output_folder,
                                           f"{os.path.splitext(os.path.basename(input_pdf_path))[0]}_page_{page_num + 1}.pdf")
            with open(output_pdf_path, 'wb') as output_pdf_file:
                pdf_writer.write(output_pdf_file)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} [input_pdfs_folder] [output_folder]")
        exit(1)

    input_pdfs_folder = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(input_pdfs_folder):
        for file in files:
            if file.lower().endswith('.pdf'):
                input_pdf_path = os.path.join(root, file)
                print(f"Processing {input_pdf_path}")
                split_pdf(input_pdf_path, output_folder)


if __name__ == "__main__":
    main()


