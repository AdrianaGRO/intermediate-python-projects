import pandas
import os


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        # Get the directory where this script is located to find data.csv
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, "data.csv")
        df = pandas.read_csv(csv_path)
        return tuple(df.loc[df['word']==self.term]['definition'])


# Test the API
# d = Definition(term="sun")
# print(d.get())