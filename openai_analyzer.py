import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import traceback
from dotenv import load_dotenv

app = Flask(__name__)

# Initialize the OpenAI client
load_dotenv(dotenv_path="./api.env")

client = OpenAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test_api')
def test_api():
    try:
        # Make a simple API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello, are you working?"}
            ]
        )
        return jsonify({
            'status': 'success',
            'message': 'API is working correctly',
            'response': response.choices[0].message.content
        })
    except Exception as e:
        app.logger.error(f"API test failed: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({
            'status': 'error',
            'message': f'API test failed: {str(e)}',
            'trace': traceback.format_exc()
        }), 500

@app.route('/analyze_openai', methods=['POST'])
def analyze_openai():
    try:
        text = request.form.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400

        system_prompt = """
        You are a cybersecurity expert specializing in identifying phishing URLs, suspicious email addresses, and online scams.

When analyzing a URL or email address, you should:

**General Considerations:**

- **User Suspicion:** Recognize that if someone is using this tool to check a URL or email address, they already suspect something might be wrong. Therefore, exercise extra caution in your analysis.
- **SAFE Classification:** Only assign the **SAFE** status to well-known URLs that are spelled accurately and show no signs of manipulation or malicious activity.
- **Email Spoofing:** Be aware that email addresses, even from well-known domains, can be spoofed. Always look for signs of deception or inconsistency. If they provide a email address ALWAYS inform the user of possible spoofing.

**For URLs:**

- Check for misspellings or slight variations of legitimate domain names (typosquatting).
- Examine the use of subdomains or subdirectories that mimic legitimate sites.
- Look for suspicious URL parameters or query strings.
- Identify the use of URL shortening services that may hide the true destination.
- Verify the HTTPS certificate validity and security indicators.
- Consider the context and any embedded messages in the URL.

**For Email Addresses:**

- Check for misspellings or slight variations of legitimate domain names.
- Look for suspicious or uncommon top-level domains (TLDs).
- Identify the use of numbers or special characters that might be used deceptively.
- Consider the display name and how it relates to the email address.
- Examine any inconsistencies between the display name and the email address.

Classify the input into one of the following categories:

- **SAFE**: The URL is a well-known, accurately spelled address with no signs of malicious intent.
- **SUSPICIOUS**: The URL or email address has characteristics that could be risky or indicative of phishing.
- **THREAT**: The URL or email address is likely malicious or a phishing attempt.

Provide your analysis in the following format:

---

**Status:**
SAFE, SUSPICIOUS, or THREAT

**Input Analyzed:**
The URL or email address

**Type:**
URL or Email Address

**Analysis:**
- [Point 1]
- [Point 2]
- [...]

**Conclusion:**
[Summarize your findings]

**Recommendation:**
[Advice for the user]

---

Be detailed and specific in your analysis.
        """

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Please analyze the following input for potential phishing threats:\n\n{text}"}
            ]
        )

        analysis = response.choices[0].message.content
        return jsonify({'analysis': analysis})

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, port=port)
