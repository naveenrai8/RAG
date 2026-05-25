from enum import Enum

def main():
    pdf_reader = Enum("pdf_reader_types", ['pymupdf', 'dummy'])
    print(pdf_reader)
    print(pdf_reader['pymupdf'])
    print(pdf_reader(1))
    print(len(pdf_reader))

if __name__ == "__main__":
    main()
