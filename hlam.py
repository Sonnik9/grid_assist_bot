
    # def cancel_order_by_id(self, symbol, last_sl_order_id):

    #     cancel_order = None
    #     all_orders = None
    #     success_flag = False
    #     all_orders = get_apii.get_all_orders()

    #     for item in all_orders:
    #         if item["symbol"] == symbol:
    #             params = {}
    #             params["symbol"] = item["symbol"]
    #             params["orderId"] = last_sl_order_id
    #             params = self.get_signature(params)
    #             url = my_params.URL_PATTERN_DICT['create_order_url']                
    #             cancel_order = self.HTTP_request(url, method=self.method, headers=self.header, params=params)                
    #             break

    #     if cancel_order and 'status' in cancel_order and cancel_order['status'] == 'CANCELED':
    #         success_flag = True 
            
    #     return cancel_order, success_flag


# Plot the Price Chart with Support and Resistance Levels
# plt.figure(figsize=(12, 6))
# plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
# plt.plot(df['Date'], df['Support1'], label='Support1', linestyle='--', color='green')
# plt.plot(df['Date'], df['Support2'], label='Support2', linestyle='--', color='orange')
# plt.plot(df['Date'], df['Support3'], label='Support3', linestyle='--', color='red')
# plt.plot(df['Date'], df['Resistance1'], label='Resistance1', linestyle='--', color='purple')
# plt.plot(df['Date'], df['Resistance2'], label='Resistance2', linestyle='--', color='brown')
# plt.plot(df['Date'], df['Resistance3'], label='Resistance3', linestyle='--', color='black')

# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.title('Price Chart with Support and Resistance Levels')
# plt.legend()
# plt.grid()

# plt.show()