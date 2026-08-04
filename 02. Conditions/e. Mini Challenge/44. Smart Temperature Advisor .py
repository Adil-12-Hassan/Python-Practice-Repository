# A Program to Advise Clothing Based on Temperature.

temperature = float(input("\nEnter temperature (°C): "))

if temperature < 10:
    print("Very Cold - Wear heavy clothes.")
elif temperature < 20:
    print("Cool - Wear a jacket.")
elif temperature < 30:
    print("Pleasant - Light clothing is fine.")
else:
    print("Hot - Stay hydrated and wear light clothes.")
    
# Explanation:
# In this code snippet, we take the temperature in degrees Celsius as input from the user. We then use if-elif-else statements to provide clothing advice based on the temperature range. If the temperature is below 10°C, we advise wearing heavy clothes. If it's between 10°C and 20°C, we suggest wearing a jacket. For temperatures between 20°C and 30°C, light clothing is recommended. Finally, if the temperature is above 30°C, we advise staying hydrated and wearing light clothes. This code helps users make appropriate clothing choices based on the current temperature.