from datasets import load_dataset

ds = load_dataset("deepset/prompt-injections")
train = ds["train"].to_pandas()
test = ds["test"].to_pandas()

train.to_csv("data/train.csv", index=False)
test.to_csv("data/test.csv", index=False)

print("Train size:", train.shape)
print("Test size:", test.shape)
print(train["label"].value_counts())
print(train.head())
