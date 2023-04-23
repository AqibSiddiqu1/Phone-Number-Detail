import phonenumbers

from phonenumbers import timezone,geocoder,carrier

number = input("Enter your Number with Country Code : ")

phone = phonenumbers.parse(number)

time= timezone.time_zones_for_number(phone)

car = carrier.name_for_number(phone,"en")

reg= geocoder.description_for_number(phone,"en")

print("\n")

print("Country Code and National Number : ",phone)

print("Time Zone : ",time)

print("Sim Company : ",car)

print("Sim Resgisteration : ",reg)
