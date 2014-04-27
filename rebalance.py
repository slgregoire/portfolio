def rebalancing():

	bond_curr = float(raw_input('What is the current dollar amount of your bond holdings? '))
	stock_us_curr = float(raw_input('What is the current dollar amount of your US stock holdings? '))
	stock_intl_curr = float(raw_input('What is the current dollar amount of your international stock holdings? '))
	contribution = float(raw_input('How much are you contributing in total? '))

	bond_allocation = float(raw_input('What is your target bond allocation? '))
	stock_us_allocation = float(raw_input('What is your target US stock allocation? '))
	stock_intl_allocation = float(raw_input('What is your target international stock allocation? '))

	total = bond_curr + stock_us_curr + stock_intl_curr + contribution

	bond_add = round(bond_allocation * total - bond_curr,2)
	stock_us_add = round(stock_us_allocation * total - stock_us_curr,2) 
	stock_intl_add = round(stock_intl_allocation * total - stock_intl_curr,2)

	contribution_rounded = bond_add + stock_us_add + stock_intl_add

	if (contribution_rounded != contribution) and (contribution_rounded < contribution):
		diff_rounded = round(contribution - contribution_rounded,2)
		stock_us_add += round(diff_rounded,2)
		print('Added excess of $' + str(diff_rounded) + ' to US stock contribution.')
	elif (contribution_rounded != contribution) and (contribution_rounded > contribution):
		print('Excess is $' + str(diff_rounded) + '.')

	print('Add $' + str(bond_add) + ' to bond funds.')
	print('Add $' + str(stock_us_add) + ' to US stock funds.')
	print('Add $' + str(stock_intl_add) + ' to international stock funds.')