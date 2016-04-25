import os
from jinja2 import Environment, FileSystemLoader
import pandas as pd

# Load Jinja2 template engine
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=FileSystemLoader(PATH),
        trim_blocks=False)


data = pd.read_csv("form.csv")
# Columns:
# "Nickname"
# "Full Name"
# "Organization"

for index, row in data.iterrows():
    nickname = row["Nickname"]
    context = {
            "nickname": row["Nickname"],
            "fullname": row["Full Name"],
            "organization": row["Organization"],
            "username_1": row["First username"],
            }
    filename = "2print-{}.svg".format(nickname)
    print("Writing {} ...".format(filename))
    with open(filename, "w") as output:
        output.write(TEMPLATE_ENVIRONMENT.get_template("badge.svg").render(context))
    print("{} finished.".format(filename))

