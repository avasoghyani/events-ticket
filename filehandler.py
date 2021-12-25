import csv
import pandas as pd


def update_colum(row_num, new_value):
    df = pd.read_csv("events.csv")
    df.loc[row_num, 'remaining capacity'] = new_value
    df.to_csv("events.csv", index=False)


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

    def find_row(self, a, b):
        with open(self.path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if row['user name'] == a and row['password'] == b:
                    return True

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

    def edit_file(self, prev_dic, new_dic):
        with open(self.path, 'r') as csvfile:
            rows = []
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                rows.append(dict(row))

        for i, j in enumerate(rows):
            for k, v in prev_dic.items():
                if j[k] == v:
                    for k2, v2 in new_dic.items():
                        rows[i][k2] = v2

        keys = rows[0].keys()
        with open(self.path, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(rows)

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
    # def edit_row(self, new_info):
    #     all_rows = self.read_csvfile_as_dictionary()
    #     final_rows = []
    #     for row in all_rows:
    #         if row["event name"] ==new_info["event name"]:
    #             row = new_info
    #         final_rows.append(row)
    #     self.write(final_rows)
