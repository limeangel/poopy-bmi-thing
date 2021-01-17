#INSTRUCTIONS
#if you want your BMi with metric measurements, type "Yes" below. to go back to imperial, type "No".
change_system = "No"
#enter your weight in pounds or kgs
weight = 126
#enter your height in ft or meters
ftheight = 5
#enter your height in Inches or leave with 0 if metric is selected
inchheight = 5
#dont touch any of this lol
ddsajfiwijsjdiaijdj = "open source bmi calculator v0.1"
print(ddsajfiwijsjdiaijdj)
disclaimer = "Ignore all text except for the top and the very bottom."
print(disclaimer)
print("-------------------------------------------------")
if change_system == "No":
exponent = 2
multip = 703
ftinchheight = ftheight * 12
height = ftinchheight + ftheight
bmi = multip * weight/ height ** exponent
print(bmi)
if bmi > 12:
  print("extremely underweight")
 
if bmi > 16:
  print("underweight")
if bmi > 18:
  print("healthy")
if bmi > 24:
  print("overweight")
if bmi > 30:
  print("obese")
if bmi > 35:
  print("Severely Obese")
if bmi > 40:
  print("MORBIDLY Obese")
if change_system == "Yes":
totalia = weight/ ftheight ** 2
print(totalia)
if totalia < 12:
  print("extremely underweight")
if totalia > 16:
  print("underweight")
if totalia > 18:
  print("healthy")
if totalia > 24:
  print("overweight")
if totalia > 30:
  print("obese")
if totalia > 35:
  print("Severely Obese")
if totalia > 40:
  print("MORBIDLY Obese")
 

