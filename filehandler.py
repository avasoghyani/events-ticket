import csv
import pandas as pd
import events


def update_colum(row_num, new_value):
    df = pd.read_csv("events.csv")
    df.loc[row_num, 'remaining capacity'] = new_value
    df.to_csv("events.csv", index=False)


def read_csv_pandas_user(file):
    df = pd.read_csv(file)
    a = df[["event name", "time of event", "place of event", "remaining capacity", "ticket fee"]]
    dff = a[a['remaining capacity'] != 0]
    print(dff.to_string())


def read_csv_pandas_admin(file):
    df = pd.read_csv(file)
    print(df.to_string())


def search_in_csv(file, row_num, colum_title):
    df = pd.read_csv(file)
    cell_value = df.loc[row_num, colum_title]
    return cell_value


def select_row_object(row_num, file):
    a = File(file).read_csvfile_as_dictionary()
    b = a[row_num]
    c = events.Events(*b.values())
    return c


class File:
    def __init__(self, path):
        self.path = path

    def read_file(self, delimeter=','):
        data = []
        with open(self.path, "r") as file:
            for line in file:
                line = line.strip()
                temp = line.split(delimeter)  # or some other preprocessing
                data.append(temp)
        return data

    def read_file_csv(self):
        with open(self.path, 'r') as csvfile:
            rows = []
            fields = []
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
        return fields, rows

    def read_csvfile_as_dictionary(self):
        with open(self.path, 'r') as csvfile:
            rows = []
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                rows.append(dict(row))
            return rows

    def show_event_for_user(self):
        with open(self.path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for i, row in enumerate(csvreader):
                print(
                    f"{i}-{row['event name']} occur at {row['time of event']} in {row['place of event']} the capacity is {row['total capacity']}" \
                    f" and remain capacity is{row['remaining capacity']} and ticket cost is {row['ticket fee']}")
            return row

    def show_event_for_admin(self):
        with open(self.path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                print(f"{row['event name']}:\n capacity: {row['total capacity']}  remaining ticket:"
                      f"{row['remaining capacity']} ticket sold: {int(row['total capacity']) - int(row['remaining capacity'])}")

    def return_row(self, username):
        with open(self.path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if row['user name'] == username:
                    return row

    def check_pass(self, password):
        with open(self.path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if row['password'] == password:
                    return True

    def check_username(self, username):
        with open(self.path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if row['username'] == username:
                    return True

    def write(self, item_dict):
        with open(self.path, 'a', newline='') as file:
            fields = list(item_dict.keys())
            writer = csv.DictWriter(file, fieldnames=fields)

            # writing headers (field names)
            if file.tell() == 0:
                writer.writeheader()

            # writing data rows
            writer.writerow(item_dict)
            file.close()

    def delete_specific_row(self, item_list):
        with open(self.path, 'r') as inp:
            reader = csv.reader(inp)
            rows = []
            for row in reader:
                if row != item_list:
                    rows.append(row)
        with open(self.path, 'w', newline='') as out:
            writer = csv.writer(out)
            for row in rows:
                writer.writerow(row)

    def select_special_row(self, num):
        with open(self.path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for i, row in enumerate(csvreader):
                if i == num:
                    return row

    def edit_row(self, new_info):
        all_rows = self.read_csvfile_as_dictionary()
        final_rows = []
        for row in all_rows:
            if row["event name"] == str(new_info["event name"]):
                row = new_info
            final_rows.append(row)
        self.write(final_rows)
