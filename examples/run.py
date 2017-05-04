import discogs_client


"""
d = discogs_client.Client('ExampleApplication/0.1')
d.set_consumer_key('CHcjnSdrYtRIRWPEjcfI',
                   'qasuBwasGGrraGIoMtOqKkssYnELwNMK')
print("Get verifier here: " + d.get_authorize_url()[2])
verifier = input("Enter verifier: ")
d.get_access_token(verifier)
"""
"""
me = d.identity()
print("I'm {0} ({1}) from {2}.".format(me.name, me.username, me.location))
print(len(me.wantlist))
me.wantlist.add(d.release(5))
print(len(me.wantlist))
"""
#"""
d = discogs_client.Client('ExampleApplication/0.1',
                          user_token="wuYMABvmUDdOMXerFacIXQBQJJphFkPgtivGgfLW")
#"""

"""
results = d.search('Stockholm By Night', type='release')
print(results.pages)

artist = results[0].artists[0]
print(artist.name)
artist = d.artist(956139)
print(artist.aliases)
print(artist.releases.page(1))

releases = d.search('Bit Shifter', type='artist')[0].releases[1].\
...        versions[0].labels[0].releases
print(len(releases))
"""
