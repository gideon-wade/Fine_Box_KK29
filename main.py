import csv
import os
import os.path

import matplotlib.pyplot as plt
import pandas as pd


def run_program():
    df = pd.read_csv('Data_files/Fine_Box_stats.csv', sep=",")
    isWeekly = True
    is_Monthly = False
    histogram_totals(df, isWeekly, is_Monthly)


def histogram_totals(df, isWeekly, is_Monthly):
    plt.bar(df['Room nr.'], df['Total fee'], color="#b21d1d")
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
    plt.ylabel('DKK')
    plt.xlabel('Room numbers')
    if not isWeekly and not is_Monthly:
        plt.title("Overview of the Semester")
    elif not isWeekly and is_Monthly:
        plt.title("Overview of the Month")
    else:
        # PATH TO YOUR /plotWeekX DIRECTORY
        plt.savefig("plotsWeekX/residents'_payments.png")
    plt.show()
    histogram_most_frequent(df, isWeekly, is_Monthly)


def histogram_most_frequent(df, isWeekly, is_Monthly):
    Rules = ['Kitchen duty', 'Minors', 'Kitchen cleaning', 'Wok pan/small pot', 'Toaster']
    Kd_total, M_total, Kc_total, W_total, T_total = (0, 0, 0, 0, 0)
    # M_total = 0
    # Kc_total = 0
    # W_total = 0
    # T_total = 0
    for x in range(17):
        Kd_total += df['Kitchen duty'][x]
        M_total += df['Minors'][x]
        Kc_total += df['Kitchen cleaning'][x]
        W_total += df['Wok pan/small pot'][x]
        T_total += df['Toaster'][x]
    frequency = [Kd_total, M_total, Kc_total, W_total, T_total]
    plt.bar(Rules, frequency, color="#e29316")
    plt.xticks(rotation=13)
    if not isWeekly and not is_Monthly:
        plt.title("Overview of the Semester")
        plt.show()
    elif not isWeekly and is_Monthly:
        plt.title("Overview of the Month")
        plt.show()
    else:
        # PATH TO YOUR /plotWeekX DIRECTORY
        plt.savefig("plotsWeekX/most_frequent.png")
        plt.show()
        update_monthly_data(df)
        update_yearly_overview(df)


def update_yearly_overview(df):
    print("Want to add this data to the semester data?")
    answer = input("Type in 'y' to add and 'n' to not add: ")
    headers = ['Room nr.', 'Total fee', 'Kitchen duty', 'Minors', 'Kitchen cleaning', 'Wok pan/small pot', 'Toaster']
    file_name_yearly = 'Data_files/Semester_Stats/Fine_Box_stats_Semester_update_'
    updates = get_file_quantity('Data_files/Semester_Stats/')
    print("Updates: " + str(updates))
    semester_dataframe = pd.read_csv(file_name_yearly + str(updates - 1) + '.csv', sep=",")
    print(df)
    print(semester_dataframe)
    print(df['Total fee'][0])
    print(semester_dataframe['Total fee'][0])
    if answer == "y":
        # open the file in the write mode
        with open(file_name_yearly + str(updates) + '.csv', 'w') as f:
            # create the csv writer
            writer = csv.writer(f)
            rows, cols = (17, 7)
            matrix = [[0] * cols for _ in range(rows)]

            # write a header-row to the csv file
            writer.writerow(headers)

            for x in range(cols):
                for y in range(rows):
                    if x == 0:
                        matrix[y][x] = y + 1
                    else:
                        if x == 1:
                            matrix[y][x] = df['Total fee'][y] + semester_dataframe['Total fee'][y]
                        if x == 2:
                            matrix[y][x] = df['Kitchen duty'][y] + semester_dataframe['Kitchen duty'][y]
                        if x == 3:
                            matrix[y][x] = df['Minors'][y] + semester_dataframe['Minors'][y]
                        if x == 4:
                            matrix[y][x] = df['Kitchen cleaning'][y] + semester_dataframe['Kitchen cleaning'][y]
                        if x == 5:
                            matrix[y][x] = df['Wok pan/small pot'][y] + semester_dataframe['Wok pan/small pot'][y]
                        if x == 6:
                            matrix[y][x] = df['Toaster'][y] + semester_dataframe['Toaster'][y]
            writer.writerows(matrix)

        print("Did you regret?")
        answer = input("'y' for yes: ")
        if answer == "y":
            regret(semester_dataframe, df)
        else:
            print("Data of semester has been updated.\n")
    else:
        print("Run program again to update the data.")


def regret(df_yearly, df):
    print("Regret.")


def get_file_quantity(Directory):
    path, dirs, files = next(os.walk(Directory))
    file_count = len(files)
    return file_count


def update_monthly_data(df):
    headers = ['Room nr.', 'Total fee', 'Kitchen duty', 'Minors', 'Kitchen cleaning', 'Wok pan/small pot', 'Toaster']
    file_name_monthly = 'Data_files/Monthly_Stats/Fine_Box_stats_Month_update_'
    updates = get_file_quantity('Data_files/Monthly_Stats/')
    print("Updates: " + str(updates))
    monthly_dataframe = pd.read_csv(file_name_monthly + str(updates - 1) + '.csv', sep=",")
    # open the file in the write mode
    with open(file_name_monthly + str(updates) + '.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        rows, cols = (17, 7)
        matrix = [[0] * cols for _ in range(rows)]

        # write a header-row to the csv file
        writer.writerow(headers)

        for x in range(cols):
            for y in range(rows):
                if x == 0:
                    matrix[y][x] = y + 1
                else:
                    if x == 1:
                        matrix[y][x] = df['Total fee'][y] + monthly_dataframe['Total fee'][y]
                    if x == 2:
                        matrix[y][x] = df['Kitchen duty'][y] + monthly_dataframe['Kitchen duty'][y]
                    if x == 3:
                        matrix[y][x] = df['Minors'][y] + monthly_dataframe['Minors'][y]
                    if x == 4:
                        matrix[y][x] = df['Kitchen cleaning'][y] + monthly_dataframe['Kitchen cleaning'][y]
                    if x == 5:
                        matrix[y][x] = df['Wok pan/small pot'][y] + monthly_dataframe['Wok pan/small pot'][y]
                    if x == 6:
                        matrix[y][x] = df['Toaster'][y] + monthly_dataframe['Toaster'][y]
        writer.writerows(matrix)


if __name__ == "__main__":
    print("Want to plot at the Semester data?")
    ans = input("'y' or 'n': ")
    if ans == "y":
        ups = get_file_quantity('Data_files/Semester_Stats/')
        semester_dataframe = pd.read_csv('Data_files/Semester_Stats/Fine_Box_stats_Semester'
                                         '_update_' + str(ups - 1) + '.csv', sep=",")
        is_Weekly = False
        is_Monthly = False
        histogram_totals(semester_dataframe, is_Weekly, is_Monthly)
    print("Want to plot at the Monthly data?")
    ans = input("'y' or 'n': ")
    if ans == "y":
        ups = get_file_quantity('Data_files/Monthly_Stats/')
        monthly_df = pd.read_csv('Data_files/Monthly_Stats/Fine_Box_stats_Month_'
                                        'update_' + str(ups - 1) + '.csv', sep=",")
        is_Weekly = False
        is_Monthly = True
        histogram_totals(monthly_df, is_Weekly, is_Monthly)
    else:
        print("Proceeding to plot data weekly data...")
        run_program()
