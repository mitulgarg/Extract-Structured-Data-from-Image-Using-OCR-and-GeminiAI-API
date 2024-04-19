OCRLLM.py first does OCR on Birth certificates using the 'pytesseract' library and extracts 'string' data 
Data is cleaned by removing redundant symbols using the 're' library 
Data is fed into Gemini AI along with a one-shot example and Unstructured data from the Image is now converted into Structured Data
Thus, a Birth certificate Image is translated into structured data.
