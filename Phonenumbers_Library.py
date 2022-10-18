import phonenumbers

from phonenumbers import geocoder,carrier,timezone
import time

number=input("\n\t Enter your number(with country code): ")

parseNumber=phonenumbers.parse(number)

print("\n\t Please wait a moment...")
time.sleep(2)

print("\n\t Country Name : ",geocoder.description_for_number(parseNumber,"en"))

print("\n\t Sim Name : ",carrier.name_for_number(parseNumber,"en"))

print("\n\t Time Zone : ",timezone.time_zones_for_number(parseNumber))
