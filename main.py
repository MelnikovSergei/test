import pandas as pd
import pprint
pp = pprint.PrettyPrinter(indent=4)

df = pd.read_csv("stack-overflow-developer-survey-2022/hui.csv")

drop_df = df.dropna()

print(drop_df)
print()


def plusser(value):
    print(value[1])
    return "hui" + str(value[1])


x = map(plusser, drop_df.iterrows())
print(x)

y = pd.DataFrame(x)
pp.pprint(y)

