import pandas as pd


class CsvFileManager:
    def __init__(self, filename: str, cols: list[str] = None):
        self.__filename = filename
        self.__df = pd.DataFrame(columns=cols) if cols else pd.DataFrame()

    def load_csv(self):
        if self.__filename:
            try:
                self.__df = pd.read_csv(self.__filename)
            except FileNotFoundError:
                print(f"the file {self.__filename} cannot be found.")
                self.__df = pd.DataFrame(columns=self.__df.columns)

    def add_line_csv(self, **kwargs):
        self.__df = self.__df._append(kwargs, ignore_index=True)

    def delete_line_csv(self, condition):
        self.__df = self.__df[~condition]

    def rename_column(self, old_name: str, new_name: str):
        if old_name in self.__df.columns:
            self.__df = self.__df.rename(columns={old_name: new_name})

    def save_csv(self):
        if self.__df.columns.empty:
            print("no column defined")
            return
        self.__df.to_csv(self.__filename, index=False)

    def create_csv_with_cols(self):
        if self.__df.columns.empty:
            print("no column defined")
            return
        self.__df.to_csv(self.__filename, index=False)
