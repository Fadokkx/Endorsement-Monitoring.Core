import base64
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os

load_dotenv()

Api_url = os.getenv("CAPTCHA_API_URL")

class CaptchaResolver:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_image(self) -> tuple[str, str]:
        img_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="no-back"]/div/div[1]/form/div[4]/div[2]/div/img')))
        captcha_url = img_element.get_attribute("src")

        print(captcha_url)
        response = requests.get(captcha_url, stream=True)
        response.raise_for_status()
        
        image_bytes = response.content
        base64_image = base64.b64encode(image_bytes).decode("utf-8")
        base64_image = f"data:image/jpeg;base64,{base64_image}"
        
        print (base64_image)
        return base64_image

    def captcha_resolver(self, base64_image: str) -> str:
        api_url = "https://api.capsolver.com/createTask"
        payload = {"dataImg": base64_image}
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            return response.json().get("text", "")
        else:
            raise Exception(f"Erro na API: {response.text}")