from flask import Flask, render_template, request
import time

app = Flask(__name__)

def pattern_search(txt, pat):
    m = len(txt)
    n = len(pat)

    for i in range(m - n + 1):
        if txt[i:n+i] == pat:
            return i
    return -1

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    exec_time = None
    txt = ""
    pat = ""

    if request.method == "POST":
        txt = request.form.get("txt", "")
        pat = request.form.get("pat", "")

        stime = time.time()
        time.sleep(1)
        result = pattern_search(txt, pat)
        etime = time.time()
        exec_time = etime - stime - 1

    return render_template(
        "index.html",
        result=result,
        exec_time=exec_time,
        txt=txt,
        pat=pat
    )

if __name__ == "__main__":
    app.run(debug=True)