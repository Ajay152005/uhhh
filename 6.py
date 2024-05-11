def vowel():
  input_vowel = eval(input("Enter the words as tuple ('word1', 'word2' ,...): "))
  
  vowel = ['a', 'e', 'i', 'o', 'u']

  voweled = []

  for word in input_vowel:
    if all(v in word for v in vowel):
      voweled.append(word)

  print(voweled)


#bmi

def bmi():
  input_bmi = eval((input("enter height and weight (height, weight): ")))
  height = input_bmi[0]
  weight = input_bmi[1]

  def get_bmi(height, weight):
    bmi = weight/(height**2)
    if bmi > 30:
      bmi_val = 'OBESE'
    elif 30 > bmi >= 25:
      bmi_val = 'OverWeight'
    elif 25 > bmi >= 18.5:
      bmi_val = 'Normal'
    else:
      bmi_val = 'UnderWeight'
    return bmi_val
  
  bmi = get_bmi(height, weight)
  print('BMI : ', bmi)

Menu = """OPTIONS:
          
          1. Type "1" for vowels.
          2. Type "2" for bmi.
          3. Type "3" to EXIT.

          Enter your option: """

while(True):

    input_val = int(input(Menu))

    if input_val == 1:
       vowel()
    elif input_val == 2:
       bmi()
    elif input_val == 3:
      break

    con = input("Do you wanna continue? (Y/N): ")
    if con == 'N':
      break