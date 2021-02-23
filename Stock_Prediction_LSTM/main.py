# Stock Prediction
# author @Yichen Wang

# Import libraries
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # Get the stock quote
    df = web.DataReader('AAPL', data_source='yahoo', start='2016-01-01', end='2021-02-16')
    # Show the data
    #print(df.shape)
    # Visualize the closing price history
    #plt.figure(figsize=(16, 8))
    #plt.title('Close Price History')
    #plt.plot(df['Close'])
    #plt.xlabel('Date', fontsize=18)
    #plt.ylabel('Close Price USD ($)', fontsize=18)
    #plt.show()

    # Create a new dataframe with only the 'Close column'
    data = df.filter(['Close'])
    dataset = data.values
    training_data_len = math.ceil(len(dataset) * .8)
    #print(training_data_len)

    # Scale the data
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)
    #print(scaled_data)

    # Create the training data set
    # Create the scaled training data set
    train_data = scaled_data[0:training_data_len, :]
    # Split the data into x_train and y_train data sets
    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i,0])
        if i<=60:
            print(x_train)
            print(y_train)

    # Convert the x_train and y_train to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)

    # Reshape the data
    print(x_train.shape)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1))) #the instruction input_shape()
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
