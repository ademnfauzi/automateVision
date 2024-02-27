from bs4 import BeautifulSoup

def extract_test_counts(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the elements containing passed and failed tests counts
    passed_count_element = soup.find('span', {'class': 'passed'})
    failed_count_element = soup.find('span', {'class': 'failed'})

    print("Passed element:", passed_count_element)
    print("Failed element:", failed_count_element)

    # Extract the numeric part of the text content and convert it to integers
    passed_count = int(''.join(filter(str.isdigit, passed_count_element.text))) if passed_count_element else 0
    failed_count = int(''.join(filter(str.isdigit, failed_count_element.text))) if failed_count_element else 0

    return passed_count, failed_count

# Example usage
with open('/Users/ade/Documents/Automation/automateVision/report/report.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

passed_count, failed_count = extract_test_counts(html_content)
print(f"Passed: {passed_count}, Failed: {failed_count}")