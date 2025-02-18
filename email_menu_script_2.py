import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()

email_password = os.getenv("EMAIL_PASSWORD")

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no browser UI)
driver = webdriver.Chrome(options=options)

try:
    # Open the target URL
    driver.get("https://mtec.revelup.online/store/4/category/65/subcategory/71")

    # Wait until the element appears in the DOM (adjust timeout if needed)

    wait = WebDriverWait(driver, 20)

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-subcategory__1__product__0"]')))
    element2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-subcategory__1__product__1"]')))

    script = "return document.querySelector('[data-testid=\"product-subcategory__1__product__0\"]').innerText;"
    extracted_text = driver.execute_script(script)
    script2 = "return document.querySelector('[data-testid=\"product-subcategory__1__product__1\"]').innerText;"
    extracted_text2 = driver.execute_script(script2)
    print("First special:", extracted_text)
    print("second special:", extracted_text2)

finally:
    driver.quit()  # Close the browser

# Email setup
sender_email = "swimmerlucy963@gmail.com"
receiver_email = "mtech-lunch-aaaapjyq4agrnhi5gbbhh2okhe@ncino.org.slack.com"
subject = "Today's Lunch Special"
body = f"Here is the lunch special:\n\n{extracted_text}\n\n{extracted_text2}"

# Create email message
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Send email using Gmail SMTP
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, email_password)  # Use App Password for security
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print("Failed to send email:", e)

