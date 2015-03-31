# Problem 5
# Maximilian Lemos

products = {'partnos':[101,253,167,331],
            'description':['x-tube','v-mesh','wahbah','zoowap'],
            'quantity':[31,12,26,15],
            'price':[3.79,.87,1.04,8.07]}

price = products.get('price')
quant = products.get('quantity')

main_total = 0
for i in range(4): 
        total = price[i] * quant[i]
        main_total = main_total + total
print(main_total)    

