import json

list_of_streamers = []  # Make list_of_streamers a list


def load():
    """Loads jsonfile called profiler.json and returns the streamerlist"""
    with open("profiler.json", "r") as f:
        streamerlist = json.load(f)
        return streamerlist

def exists(name):
    """Check if (name) is in list_of_streamers"""
    for bla in list_of_streamers:
        if bla.name == name:
            print("Streamer is in list")
            break
    else:
        print("Streamer is not in list")


def save():
    """Save Jsonfile"""
    with open("profiler.json", "w") as f:
        o = json.dumps(loop, indent=2)
        f.write(o)


class Streamer:
    def __init__(self, name=None, uid=None, birthday=None, age=None, job=None, favor=None, relationship=None,
                 location=None, link=None, tags=None):
        """Returns Streamer(Object)"""
        self.name = name
        self.uid = uid
        self.birthday = birthday
        self.age = age
        self.job = job
        self.favor = favor
        self.relationship = relationship
        self.location = location
        self.link = link
        self.tags = tags

    def add(self):
        """Add Streamer to json"""
        added_streamer = {
            "name": self.name,
            "id": self.uid,
            "birthday": self.birthday,
            "age": self.age,
            "job": self.job,
            "favor": self.favor,
            "relationship": self.relationship,
            "location": self.location,
            "link": self.link,
            "tags": self.tags}
        loop.append(added_streamer)

    def edit(self, name=None, uid=None, birthday=None, age=None, job=None, favor=None, relationship=None,
             location=None, link=None, tags=None):
        for editable in loop:
            if editable['name'] == self:
                if name != None:
                    editable['name'] = name
                if uid != None:
                    editable['uid'] = uid
                if birthday != None:
                    editable['birthday'] = birthday
                if age != None:
                    editable['age'] = age
                if job != None:
                    editable['job'] = job
                if favor != None:
                    editable['favor'] = favor
                if relationship != None:
                    editable['relationship'] = relationship
                if location != None:
                    editable['location'] = location
                if link != None:
                    editable['link'] = link
                if tags != None:
                    editable['tags'] = tags
                save()
                break
        else:
            print("Streamer not found")

    def remove(self):
        """Remove Streamer matching name from json"""
        testing = Streamer(name=self)
        for test in loop:
            if test['name'] == testing.name:
                removed_streamer = {
                    "name": testing.name,
                    "id": testing.uid,
                    "birthday": testing.birthday,
                    "age": testing.age,
                    "job": testing.job,
                    "favor": testing.favor,
                    "relationship": testing.relationship,
                    "location": testing.location,
                    "link": testing.link,
                    "tags": testing.tags}
                loop.remove(removed_streamer)
                break
        else:
            print("Streamer not found")


# Load json
loop = load()
# For every streamer in json add streamer object to list_of_streamers
for st in loop:
    st = Streamer(name=st['name'], uid=st['id'], birthday=st['birthday'], age=st['age'], job=st['job'],
                  favor=st['favor'], relationship=st['relationship'],
                  location=st['location'], link=st['link'], tags=st['link'])
    list_of_streamers.append(st)

# Example of a Streamer object creation
# user = Streamer(name="bla", uid=1252, age=32)

# Get streamer and add streamer to json
# get = Streamer(name="bla", uid=5259, job="arbeitslos")
# Streamer.add(get)

# Edit info about a streamer
Streamer.edit("bla", birthday=25011956)

# Remove streamer matching name
# Streamer.remove("Joel")

# Print json
print(loop)

# Save json
save()
