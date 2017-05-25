from flask import Flask, render_template, request, jsonify
import discogs_client
import modules.process as map_process

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("mapchart.html")


@app.route("/build_mapchart", methods=["GET"])
def build_mapchart():
    client = discogs_client.Client('ExampleApplication/0.1',
                              user_token="wuYMABvmUDdOMXerFacIXQBQJJphFkPgtivGgfLW")

    type = request.args.get('type', 0, type=str)
    style = request.args.get('style', 0, type=str)
    year = int(request.args.get('year', 0, type=int))

    process = map_process.ProcessMap(client, "countries.txt")
    process.request_values("", read_file="style-countries.txt", type=type, style=style, year=year)
    #data = process.percentage_list(add_values=True)
    data = process.values_list()
    data.insert(0, ["Country", "Releases"])
    print(data)
    return jsonify(result=data)


if __name__ == "__main__":
    app.run(debug=True)
