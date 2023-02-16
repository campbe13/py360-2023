# write & test a function that calculates  tip, GST PST, and cost of meal 
# parameters cost of meal and tip as percent
# returns  total cost, tax  and tip
# pmcampbell - together
# 2023-02-14

# test the function

'''
calc tip, gst/pst & cost
test:  11.45, 20%  returns 15.46, gst/pst 1.72, tip 2.29
'''
def cost_of_meal(meal, tip_percent):
  # for arguments sake we combing GST & PST
  GSTPST =  0.15 # constant so all UPPER
  tax = meal * GSTPST 
  #print(tax)
  tip = meal * tip_percent
  #print(tip)
  tax = round(tax,2)
  tip = round(tip,2)
  total = meal + tax + tip
  return total, tax, tip

print(cost_of_meal(11.45, .2))
total, tax, tip = cost_of_meal(11.45,.2)
print (f'Your meal 11.45 + tip {tip} + tax {tax} total {total}')
