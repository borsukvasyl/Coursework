import modules.process as process
import discogs_client


def save_data(filename):
    """
    Saves requested data to filename
    :param filename: filename where data will be saved
    :return: None
    """
    with open(filename, "w") as file:
        file.write("style\n")

        # creating client
        client = discogs_client.Client('ExampleApplication/0.1',
                                       user_token="wuYMABvmUDdOMXerFacIXQBQJJphFkPgtivGgfLW")
        a = process.ProcessMap(client, "countries.txt")

        # saving additional data
        a.request_additional(type="release", year=2016)
        result = []
        for element in a._elements:
            result.append(element.additional)
        file.write("{}\n".format(str(result)))
        print(result)

        # reading key elements
        with open("styles.txt", "r")as file:
            styles = [line.strip() for line in file.readlines()]

        # saving main data
        for style in styles:
            a.request_values("", type="release", year=2016, style=style)
            result = []
            for element in a._elements:
                result.append(element.value)
            file.write("{}\t{}\n".format(style, result))
            print("{} {}".format(style, result))
