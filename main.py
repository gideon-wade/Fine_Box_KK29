import pandas as pd
import matplotlib.pyplot as plt
import csv


def run_program():
    df = pd.read_csv('Data_files/Fine_Box_stats.csv', sep=",")
    histogram_totals(df)


def histogram_totals(df):
    plt.bar(df['Room nr.'], df['Total fee'], color="#b21d1d")
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    plt.ylabel('DKK')
    plt.xlabel('Room numbers')
    # PATH TO YOUR /plotWeekX DIRECTORY
    plt.savefig("C:/Users/Gideon/PycharmProjects/Fine_Box_Template/plotsWeekX/residents'_payments.png")
    plt.show()
    histogram_most_frequent(df)


def histogram_most_frequent(df):
    Rules = ['Kitchen duty', 'Minors', 'Kitchen cleaning', 'Wok pan/small pot', 'Toaster']
    Kd_total = 0
    M_total = 0
    Kc_total = 0
    W_total = 0
    T_total = 0
    for x in range(17):
        Kd_total += df['Kitchen duty'][x]
        M_total += df['Minors'][x]
        Kc_total += df['Kitchen cleaning'][x]
        W_total += df['Wok pan/small pot'][x]
        T_total += df['Toaster'][x]
    frequency = [Kd_total, M_total, Kc_total, W_total, T_total]
    plt.bar(Rules, frequency, color="#e29316")
    plt.xticks(rotation=13)
    # PATH TO YOUR /plotWeekX DIRECTORY
    plt.savefig("C:/Users/Gideon/PycharmProjects/Fine_Box_Template/plotsWeekX/most_frequent.png")
    plt.show()
    update_yearly_overview(df)


def update_yearly_overview(df):
    print("Want to add this data to the yearly overview? ")
    answer = input("Type in 'y' to add and 'n' to not add: ")
    headers = ['Room nr., Total fee, Kitchen duty, Minors, Kitchen cleaning, Wok pan/small pot, Toaster']
    df_yearly = pd.read_csv('Data_files/Fine_Box_stats_YEARLY.csv', sep=",")
    print(df['Total fee'][0])
    print(df_yearly['Total fee'][0])
    if answer == "y":
        # open the file in the write mode
        with open('Data_files/Fine_Box_stats_YEARLY.csv', 'w') as f:
            # create the csv writer
            writer = csv.writer(f)
            rows, cols = (17, 6)
            matrix = [[0] * cols for _ in range(rows)]

            # write a row to the csv file
            writer.writerow(headers)

            for x in range(cols):
                for y in range(rows):
                    if x == 0:
                        matrix[y][x] = df['Total fee'][y] + df_yearly['Total fee'][y]
                    if x == 1:
                        matrix[y][x] = df['Kitchen duty'][y] + df_yearly['Kitchen duty'][y]
                    if x == 2:
                        matrix[y][x] = df['Minors'][y] + df_yearly['Minors'][y]
                    if x == 3:
                        matrix[y][x] = df['Kitchen cleaning'][y] + df_yearly['Kitchen cleaning'][y]
                    if x == 4:
                        matrix[y][x] = df['Wok pan/small pot'][y] + df_yearly['Wok pan/small pot'][y]
                    if x == 5:
                        matrix[y][x] = df['Toaster'][y] + df_yearly['Toaster'][y]
            print(matrix)
            string = ""
            for x in range(rows):
                for y in range(cols):
                    if y == cols - 1:
                        string += str(matrix[x][y])
                    else:
                        string += str(matrix[x][y]) + ","
                list_string = [string]
                writer.writerow(list_string)
                string = ""
        for x in range(rows):
            df_yearly['Total fee'][x] += df['Total fee'][x]
            df_yearly['Kitchen duty'][x] += df['Kitchen duty'][x]
            df_yearly['Minors'][x] += df['Minors'][x]
            df_yearly['Kitchen cleaning'][x] += df['Kitchen cleaning'][x]
            df_yearly['Wok pan/small pot'][x] += df['Wok pan/small pot'][x]
            df_yearly['Toaster'][x] += df['Toaster'][x]

        print("Did you regret?")
        answer = input("'y' for yes: ")
        if answer == "y":
            regret(df_yearly, df)
        else:
            print("Yearly overview has been updated")
    else:
        print("Run program again to update the data.")


def regret(df_yearly, df):
    print("Regret.")


if __name__ == "__main__":
    run_program()
