def weight_on_planets():
   earthWeight = int(input('What do you weigh on earth? '))
   marsWeight = earthWeight * .38
   jupiterWeight = earthWeight * 2.34
   mMes = "\nOn Mars you would weigh"
   jMes = "On Jupiter you would weigh"
   print(mMes, marsWeight, "pounds.\n" + jMes, jupiterWeight, "pounds.")
   
   
   
if __name__ == '__main__':
   weight_on_planets()