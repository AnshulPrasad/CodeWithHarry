from pypdf import PdfReader, PdfWriter
import os

writer = PdfWriter()

dir_path = "/home/anshul/Documents/CodeWithHarry/pdf"
for file in sorted(os.listdir(dir_path)):
    if file.lower().endswith(".pdf"):
        try:
            file_path = os.path.join(dir_path, file)
            reader = PdfReader(file_path)
            if reader.is_encrypted:
                reader.decrypt("")

            for page in reader.pages:
                writer.add_page(page)
        except Exception as e:
            print(f"Skipping {file}: {e}")

with open("pdf/merged.pdf", "wb") as f:
    writer.write(f)
