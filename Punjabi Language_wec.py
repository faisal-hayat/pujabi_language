import pandas as pd
from jiwer import wer

print(f'pandas version is : {pd.__version__}')

# !pip install openpyxl

data = pd.read_excel('Assets/checforWER.xlsx')
print(f'data head is : {data.head()}')

wec_scores = []
rows = data.shape[0]
for row in range(rows):
    first_sentence = data.iloc[row][0]
    second_sentence = data.iloc[row][1]
    print(f'first is : {first_sentence}, second is : {second_sentence}')
    error = wer(first_sentence, second_sentence)
    print(f'error is : {error}')
    wec_scores.append(error)

columns = data.columns
print(f'columns are : {columns}')

results = {
    'orignal sentence': data['orignal sentence '],
    'simplified sentence': data['simplified sentence '],
    'error': wec_scores
}

results = pd.DataFrame(results)
results.to_csv('Assets/error_score.csv', index=False)

print(f'final results are : {results}')
