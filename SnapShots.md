📸 Project Snapshots: URL Shortener API
This section demonstrates key features of the Flask-based URL shortener API running locally on localhost:5000.

🚀 App Running on Localhost
The Flask app is up and running on port 5000.

<img width="839" height="358" alt="Localhost Running" src="https://github.com/user-attachments/assets/535f1e73-3f9f-4bef-929c-828ca754c8c9" />
🔗 Task 1: Shorten URL Endpoint
Endpoint: POST /api/shorten
Action: Accepts a long URL and returns a shortened code.
Input URL:
https://atikvibs1326.github.io/Portfolio-Atikraja.github.io/

<img width="1362" height="899" alt="Shorten URL Request" src="https://github.com/user-attachments/assets/f7ba1c2e-3103-4b75-8a73-5522c31ddae3" />
↪️ Task 2: Redirect to Original URL
Endpoint: GET /<short_code>
Action: Redirects the user to the original URL using the short code.
Example URL: http://localhost:5000/cRRc7E

<img width="1365" height="959" alt="Redirect Using Short Code" src="https://github.com/user-attachments/assets/979e1ce8-ab76-4577-9656-cd07490e2d31" />
📊 Task 3: Analytics for Short Code
Endpoint: GET /api/stats/<short_code>
Action: Returns statistics like:

Original URL

Click count

Timestamp of creation

Orignal Url link 

<img width="1348" height="894" alt="Analytics Endpoint" src="https://github.com/user-attachments/assets/6d2f2d48-de03-4637-9c02-564e80d502e0" />
