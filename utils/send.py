import requests
from bs4 import BeautifulSoup

# Function to extract test counts from HTML
def extract_test_counts(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    passed_count_element = soup.find('span', {'class': 'passed'})
    failed_count_element = soup.find('span', {'class': 'failed'})
    passed_count = int(''.join(filter(str.isdigit, passed_count_element.text))) if passed_count_element else 0
    failed_count = int(''.join(filter(str.isdigit, failed_count_element.text))) if failed_count_element else 0
    return passed_count, failed_count

# Example usage
with open('/Users/ade/Documents/Automation/automateVision/report/report.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

passed_count, failed_count = extract_test_counts(html_content)
print(f"Passed: {passed_count}, Failed: {failed_count}")


# Send Discord
# Discord webhook setup
webhook_url = 'https://discord.com/api/webhooks/1211947885659430912/2MJhfYavdeWCJKeQQhGL48C31IswE_SI6uIkWqy74wohed_7w408h0E1sAPyrHuYeZd9'

# Create a payload with the message and file
payload = {
    'content': f"**Result Report Automation**\nPassed: {passed_count}, Failed: {failed_count}",
}

files = {
    # 'file': ('report.html', open('/Users/ade/Documents/Automation/automateVision/report/report.html', 'rb'))
}

# Make a POST request to the Discord webhook URL
response = requests.post(webhook_url, data=payload, files=files)

# Check the response status
if response.status_code == 204:
    print("Message sent successfully")
else:
    print(f"Failed to send message. Status code: {response.status_code}, Response content: {response.text}")
