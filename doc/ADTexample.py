import discogs_client
import doc.info_processing as info_processing


d = discogs_client.Client('ExampleApplication/0.1',
                          user_token="wuYMABvmUDdOMXerFacIXQBQJJphFkPgtivGgfLW")

a = info_processing.InfoProcessing(d)

a.search("table", type="release", year=2000)
a.filter_info("style")
print("The most popular style in 2000 amount releases with \"table\"", a.the_most_used())
print("The least popular style in 2000 amount releases with \"table\"", a.the_least_used())
print()
b = d.search("table", type="release", year=2000, style="Experimental")
for i in b:
    if i not in a._filtered_info["Experimental"]:
        print(False)
