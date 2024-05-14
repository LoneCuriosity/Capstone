import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os

#i2c_data_folder = "../i2c/i2c_data"
#spi_data_folder = "../spi/spi_data"
usart_data_folder = "../usart/usart_data"

#Todo: create one model with all protocals and different boards
'''for data_folder in [i2c_data_folder, spi_data_folder, usart_data_folder]:
    for board in os.listdir(data_folder):
        data = []
        
        if len(os.listdir(f"{data_folder}/{board}/datasets")) > 1:
            for baudrates in os.listdir(f"{data_folder}/{board}/datasets"):
                print(f"Processing {data_folder}/{board}/datasets/{baudrates}/boards_dataset.csv")
                df = pd.read_csv(f"{data_folder}/{board}/datasets/{baudrates}/boards_dataset.csv")
                data.append(df)
            
            df = pd.concat(data)
        else:
            print(f"Processing {data_folder}/{board}/datasets/boards_dataset.csv")
            df = pd.read_csv(f"{data_folder}/{board}/datasets/boards_dataset.csv")
            data.append(df)
            
            df = pd.concat(data)'''
            
#only usart arduino mega       
data = []

for baudrates in os.listdir(f"{usart_data_folder}/arduino_mega/datasets"):
    print(f"Processing {usart_data_folder}/arduino_mega/datasets/{baudrates}/boards_dataset.csv")
    df = pd.read_csv(f"{usart_data_folder}/arduino_mega/datasets/{baudrates}/boards_dataset.csv")
    data.append(df)

df = pd.concat(data)

X = df.drop('label', axis=1)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier()
X_train = X_train.values
rf_classifier.fit(X_train, y_train)

X_test = X_test.values
accuracy = rf_classifier.score(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

new_data = [[4.9989503165,0.0063408164,0.0511090396,0.0000402060,0.0026121339,-6.1358363154,21.2271196063,46.1958954026,472.6730254886,4.9989543379,0.0512583543,24.9895444724,0.0026274189,5.0000000000,1.1435285501,4.7415082247,-0.1725821711,0.0000413078]]
prediction = rf_classifier.predict(new_data)
print(f"Predicted board and protocol: {prediction[0]}")