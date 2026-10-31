from flask import Flask, request, render_template_string
import base64
import codecs

app = Flask(__name__)

HTML = """
<h1>Custom Payload Encoder & Decoder</h1>
<form method="POST">
<textarea name="text" placeholder="Enter text" required></textarea>
<br><br>
<select name="method">
<option value="base64">Base64 Encode</option>
<option value="decode">Base64 Decode</option>
<option value="rot13">ROT13</option>
</select>
<br><br>
<button type="submit">Submit</button>
</form>
<h3>Result:</h3>
<pre>{{ result }}</pre>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        method = request.form.get("method")

        try:
            if method == "base64":
                result = base64.b64encode(
                    text.encode()
                ).decode()

            elif method == "decode":
                result = base64.b64decode(
                    text, validate=True
                ).decode()

            elif method == "rot13":
                result = codecs.encode(text, "rot_13")

        except Exception:
            result = "Invalid input. Please try again."

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run()
