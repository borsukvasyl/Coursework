import modules.process as process


import discogs_client


with open("styles.txt", "r")as file:
    styles = [line.strip() for line in file.readlines()]

with open("style-countries.txt", "w") as file:
    file.write("style\n")

    # creating client
    d = discogs_client.Client('ExampleApplication/0.1',
                              user_token="wuYMABvmUDdOMXerFacIXQBQJJphFkPgtivGgfLW")
    a = process.ProcessMap(d, "countries.txt")

    # saving additional data
    a.request_additional(type="release", year=2016)
    result = []
    for element in a._elements:
        result.append(element.additional)
    file.write("{}\n".format(str(result)))
    print(result)

    # saving main data
    for style in styles:
        a.request_values("", type="release", year=2016, style=style)
        result = []
        for element in a._elements:
            result.append(element.value)
        file.write("{}\t{}\n".format(style, result))
        print("{} {}".format(style, result))
