# coding: utf-8

from core import OcrClient

client = OcrClient()

print(client.extract_text_from_image('test/test_cht.jpg', language="TRADITIONAL CHINESE"))