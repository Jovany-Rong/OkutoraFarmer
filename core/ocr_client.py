# coding: utf-8

import pytesseract
from core.image_utils import load_img_from_file

# Default tesseract command path, if you put tesseract binary into PATH, you can use it.
DEFAULT_TESSERACT_CMD = 'tesseract'
# Mappings of languages and tesseract language codes.
LANG_MAPPING = {
    "ENGLISH": "eng",
    "SIMPLIFIED CHINESE": "chi_sim",
    "TRADITIONAL CHINESE": "chi_tra",
    "JAPANESE": "jpn",
    "KOREAN": "kor"
}

class OcrClient(object):
    def __init__(self, tesseractCmdPath=None):
        """Initiate an OCR Client.

        Args:
            tesseractCmdPath (str, optional): Path of tesseract executable binary. Defaults to None.
        """
        # Set tesseract command path of pytesseract.
        if tesseractCmdPath == None:
            tesseractCmdPath = DEFAULT_TESSERACT_CMD
        pytesseract.pytesseract.tesseract_cmd = tesseractCmdPath
        
        # Get available languages of tesseract.
        try:
            self.availableLanguageList = pytesseract.get_languages(config='')
        except Exception as e:
            print('No tesseract command found.')
            raise e


    def extract_text_from_image(self, imagePath, language=None):
        """Use tesseract to extract text from a given image file.

        Args:
            imagePath (str): Image file path.
            language (str, optional): Language, if it is None, tesseract will concern it as ENGLISH. Available values are: ENGLISH, SIMPLIFIED CHINESE, TRADITIONAL CHINESE, JAPANESE and KOREAN. Defaults to None.

        Raises:
            IOError: A wrong language is given.

        Returns:
            str: Text extracted from the image.
        """
        if language == None:
            language = "ENGLISH"
        langCode = LANG_MAPPING.get(language, None)
        if langCode == None:
            raise IOError("No language code found of '%s'." % language)
            return ''
        if langCode not in self.availableLanguageList:
            raise IOError("Language code '%s' not available in your tesseract environment." % langCode)
            return ''
        img = load_img_from_file(imagePath)
        if img == None:
            # If it is not an image file, return a "" string.
            return ''
        
        text = pytesseract.image_to_string(img, langCode, config=r'--psm 3')
        return text

        

    
    