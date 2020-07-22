import pandas

# core structure: DataFrame
# data2.head(n), display the first n lines of the data, default is 5
# data2.tail(n), display the last n lines of the data, default is 5
data2 = pandas.read_csv("table.csv")
print(data2.columns)
print(data2.dtypes)
print(data2.shape)
print(data2.tail())


def convert(n):
    if n > 100 or n < 0:
        raise ValueError
    elif n > 97:
        return 4.0
    elif n > 94:
        return 3.94
    elif n > 90:
        return 3.83
    elif n > 87:
        return 3.74
    elif n > 84:
        return 3.55
    elif n > 80:
        return 3.32
    else:
        return 0


gpa = data2["Score"].apply(convert)
data2["GPA"] = gpa
print(data2)

# Get elements
print(data2.loc[2])
print(data2.loc[1:3])
print(data2.loc[[1,2]])
print(data2["Name"])
# Get column names
print(data2.columns.tolist())
# Columns with the samw dimension can do operations
print(data2["Score"]*data2["GPA"])
