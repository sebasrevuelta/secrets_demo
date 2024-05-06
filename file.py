password = "aaaaa"

credentials = {}
credentials.username = "jonny"
credentials.password = "aaaa"
credentials.password1 = ""
credentials.a = 1

# ruleid: mongo
connection_string = "mongodb+srv://username:{}@{mongodbdb_host}/?retryWrites=true&w=majority".format(credentials.password)
# ruleid: mongo
connection_string = "mongodb://{}:{}@{mongodbdb_host}/?retryWrites=true&w=majority".format(credentials.username,credentials.password)
# ok: mongo
connection_string = f"mongodb://{credentials.username}:{credentials.password}@{foo}/?retryWrites=true&w=majority"
# ok: mongo
connection_string = f"mongodb://{credentials.username}:{credentials.password1}@{foo}/?retryWrites=true&w=majority"
# ok: mongo
connection_string = (
    f"mongodb://username:{credentials.a}@{mongodbdb_host}/?retryWrites=true&w=majority"
)
