import  requests
import matplotlib.pyplot as plt
from matplotlib import style
ticker_api_url = 'https://api.coinmarketcap.com/v1/ticker/'
crypto=[input('which crypto do you want to use?: '), input('which crypto do you want to compare with?: ') ] #crypto= list of 2 coins. one compare to another
def get_24h_last_change(crypto):            #give the percent of 24h crypto
    response = requests.get(ticker_api_url + crypto)
    response_json = response.json()
    return float(response_json[0]["percent_change_24h"])

def get_1h_last_change(crypto):
    response = requests.get(ticker_api_url + crypto)
    response_json = response.json()
    return float(response_json[0]["percent_change_1h"])

def get_7d_last_change(crypto):            #give the percent of 24h crypto
    response = requests.get(ticker_api_url + crypto)
    response_json = response.json()
    return float(response_json[0]["percent_change_7d"])



# x axis values

y = [get_1h_last_change(crypto[0]) ,get_24h_last_change(crypto[0]), get_7d_last_change(crypto[0])]
# corresponding y axis values
y1 = [get_1h_last_change(crypto[1]) ,get_24h_last_change(crypto[1]), get_7d_last_change(crypto[1])]
x = [1, 24, 168]

# plotting the points
plt.plot(x, y,'g',label='line one',linewidth=2)
plt.plot(x, y1,'c',label='line tow',linewidth=2)
# naming the x axis
plt.xlabel('history time (hours)')
# naming the y axis
plt.ylabel('percent of change')

# giving a title to my graph
plt.title('percent of value change')
plt.text( 155,get_7d_last_change(crypto[0]), crypto[0], horizontalalignment='left', size='medium', color='black')
plt.text( 155,get_7d_last_change(crypto[1]), crypto[1], horizontalalignment='left', size='medium', color='black')
plt.show()


