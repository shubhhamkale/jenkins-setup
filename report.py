import requests
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def run_tests_and_send_report():
    # Run pytest to generate the report.html file
    subprocess.run(
        ["pytest", "--html=report.html", "--self-contained-html", "-m", "hello"]
    )

    # Read the content of the report.html file
    with open("report.html", "r") as f:
        report_content = f.read()

    # print(type(report_content))
    # payload_headers = {
    #     "Authorization": "Bearer MTQ2Y2ZkYmMtZTg0ZS00ZmUyLWIwNTEtYTZiM2JjMWM2Yjk0.de657f0ec18252f95406a5339e4a379a43bef5e8f2f0356b7d6219e2cb5db4f44486cf76cbb7adf92ea01370264094be37540eb5adb1cd14f5d6cb9f974b2285.XNtcLLL7kAaui9lh6lh+LA=="
    # }

    # response = requests.post(
    #     "https://api.nmedia2.com/api/v1.0/upload/report",
    #     json=report_content,
    #     headers=payload_headers,
    # )
    # print(response.text)
    send_email("hello hi there")


def send_email(link):
    # list of email_id to send the mail
    try:
        li = ["shubham.kale@opsfuse.com", "sumit@opsfuse.com"]

        for dest in li:
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.login("shubhamkale325@gmail.com", "ciuzutrmqbgmwcom")
            message = MIMEMultipart("alternative")
            message["Subject"] = "Report for XYZ Project"
            message["From"] = "xyz-automation"
            message["To"] = dest

            html = """
            <html>
                <body>
                    <h1>Report for XYZ Project</h1>
                    <p>Hello,</p>
                    <p>Please find the report for the XYZ project below:</p>
                    <ul>
                        <li>Date: July 31, 2023</li>
                        <li>Report link: <a href="https://example.com/report">Click here</a></li>
                        <!-- You can include more details here, like charts, graphs, etc. -->
                    </ul>
                    <p>Thank you!</p>
                </body>
            </html>
            """

            # Attach the HTML content to the email
            part = MIMEText(html, "html")
            message.attach(part)

            # Send the email
            s.sendmail("shubhamkale325@gmail.com", dest, message.as_bytes())
            s.quit()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    run_tests_and_send_report()
