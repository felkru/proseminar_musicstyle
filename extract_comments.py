import fitz  # PyMuPDF
import os

def extract_pdf_comments_with_context(pdf_path):
    """
    Extracts all text and highlight annotations from a PDF file,
    along with the text that is highlighted or associated with the comment.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return

    try:
        doc = fitz.open(pdf_path)
        print(f"Successfully opened {pdf_path}\n")
        comment_count = 0

        for page_num, page in enumerate(doc):
            # Get all words on the page along with their bounding boxes
            words = page.get_text("words")
            
            for annot in page.annots():
                # 8 = Text annotation, 9 = Highlight annotation
                if annot.type[0] in [8, 9]: 
                    # Get the bounding box of the annotation
                    annot_rect = annot.rect
                    
                    # Extract the text that is inside the annotation's bounding box
                    highlighted_text = " ".join(w[4] for w in words if fitz.Rect(w[:4]).intersects(annot_rect))
                    
                    comment_text = annot.info.get("content", "(No comment text)")
                    
                    print(f"--- Page {page_num + 1} ---")
                    if highlighted_text:
                        print(f"Highlighted Text: \"{highlighted_text}\"")
                    print(f"Comment: {comment_text}\n")
                    
                    comment_count += 1
        
        if comment_count == 0:
            print("No text or highlight comments found in the document.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'doc' in locals():
            doc.close()

if __name__ == "__main__":
    extract_pdf_comments_with_context("feedback_igor.pdf")
