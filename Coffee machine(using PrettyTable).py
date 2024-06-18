#  Coffee machine

from prettytable import PrettyTable
table= PrettyTable()
lists=PrettyTable()
storage= PrettyTable()
coinss=PrettyTable()


coinss.add_column(' ',[''])
coinss.add_column('Coins',[''])
coinss.add_column('Value',[''])
coinss.add_column('Amount',[''])
coin_list=['Penny','Nickel', 'Dime', 'Quarter']
coffee_list=['Espresso','Latte','Capuccino']
change=0

table.add_column('Coins',['Penny','Nickel','Dime','Quarter'])
table.add_column('Value',['0.01','0.05','0.1','0.25'])
table.align='c'
coins={
	'Penny':0.01,
	'Nickel':0.05,
	'Dime':0.1,
	'Quarter':0.25
	}
lists.add_column('Coffee',['Espresso','Latte','Capuccino'])
lists.add_column('Price',['1.5','2.5','3.0'])
lists.add_column('Water',['50','200','250'])
lists.add_column('Coffee',['18','24','24'])
lists.add_column('Milk',['---','150','100'])

lists.align='c'
print(table) 
print(lists)

coffees= {'Espresso': {
            'price':1.5,
            'water': 50,
            'coffee': 18},
        'Latte': {
            'price': 2.5,
            'water': 200,
            'coffee': 24,
            'milk': 150},
        'Capuccino': {
            'price': 3.0,
            'water': 250,
            'coffee': 24,
            'milk': 100}
}

Ingredients= {'water': 300,
              'milk': 200,
              'coffee': 100,
          	'balance':0}
storage.add_column('Ingredients',['water','milk','coffee',])
storage.add_column('Amount',['300','200','100',])
print(storage)
report= f'Water: {Ingredients["water"]},\nmilk: {Ingredients["milk"]},\ncoffee: {Ingredients["coffee"]}' 

coffee_machine= True
while coffee_machine:
	balance=0
	print(f'What would you like: {coffee_list}')
	choice= input(f'What would you like: {coffee_list}').title()
	print(choice)
	report= f'Water: {Ingredients["water"]},\nmilk: {Ingredients["milk"]},\ncoffee: {Ingredients["coffee"]}'
	if choice in coffee_list:
		for i in range(len(coin_list)):
			x= coin_list[i]
			coin = float(input(f'Enter {x} you have: '))
			print(f'Enter {x} you have: {coin} ')
			balance1=round(float(coins[x])*coin,3)
			print(f'{float(coins[x])}*{coin}={balance1}')
			balance+=balance1
			
			coinss.add_row(['Entered coin_list:',x,coin,balance1])
			print(coinss)
		rounded_balance= round(balance,3)
		def check_ingredients():	
			if choice!='Espresso' and choice in coffee_list and int(coffees[choice]["water"])<int(Ingredients['water']) and int(coffees[choice]["milk"])<int(Ingredients["milk"]) and int(coffees[choice]["coffee"])<int(Ingredients['coffee']):
				print(f'Enough ingredients to make {choice})')
				return True
			elif choice=='Espresso' and choice in coffee_list and int(coffees[choice]["water"])<int(Ingredients['water']) and int(coffees[choice]["coffee"])<int(Ingredients['coffee']):
				return True
			else:
				print(f'Sorry, no resources to make {choice}(')
				if int(coffees[choice]["water"])>int(Ingredients['water']):
					print('Sorry, there is no enough water.')
					return False
				elif choice!='Espresso' and int(coffees[choice]["milk"])>int(Ingredients["milk"]):
					print('Sorry, there is no enough milk')
					return False
				elif int(coffees[choice]["coffee"])>int(Ingredients['coffee']):
					print('There is no enough coffee.')
					return False

		def check_coins():
			if check_ingredients()==True:
				if rounded_balance>=float(coffees[choice]['price']):
					change= rounded_balance-float(coffees[choice]['price'])
					print(f'It is your change: {change}')
					return True
				elif rounded_balance<float(coffees[choice]['price']):
					change= rounded_balance
					print(f'It is not enough to make a coffee(. Your coins are {rounded_balance}, and {choice} costs {coffees[choice]["price"]}. It is your refunded coins: {change}')
			else:
				change= rounded_balance
				print(f'It is your refunded coins: {change}')
				return False
		if check_coins()==True and check_ingredients()==True:
			if choice!='Espresso':
				Ingredients['water']-=int(coffees[choice]["water"])
				Ingredients['milk']-=int(coffees[choice]["milk"])
				Ingredients['coffee']-=int(coffees[choice]["coffee"])
				report= f'Water: {Ingredients["water"]},\nmilk: {Ingredients["milk"]},\ncoffee: {Ingredients["coffee"]}'

			else:
				Ingredients['water']-=int(coffees[choice]["water"])
				Ingredients['coffee']-=int(coffees[choice]["coffee"])
				report= f'Water: {Ingredients["water"]},\nmilk: {Ingredients["milk"]},\ncoffee: {Ingredients["coffee"]}'
			coinss.clear_rows()	
		else:
			print(report)
			break
	elif choice== 'Report':
		print(report)
	elif choice=='Exit':
		print('You wanted to stop!')
		break
