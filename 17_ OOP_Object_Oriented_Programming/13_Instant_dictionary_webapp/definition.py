import pandas as pd




class Definition:
    """
    A class to fetch the definition of a word using a dictionary csv file.
    """

    def __init__(self, term):
            self.term = term
            
            
    def get_definition(self):
        import os
        # Get the directory where this file is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, "data.csv")
        df = pd.read_csv(csv_path)
        definition = df[df['word'] == self.term]['definition'].values
        if len(definition) > 0:
            return definition[0]
        else:
            return "Definition not found."

# Test code - only run when script is executed directly
if __name__ == "__main__":
    d = Definition("example")
    print(d.get_definition())