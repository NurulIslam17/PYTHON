import phonenumbers
from testPhone import  number

from  phonenumbers import  geocoder
c_name=phonenumbers.parse(number,"CH")
counName=geocoder.description_for_number(c_name,"en")
print(counName)


from  phonenumbers import carrier
survice_name=phonenumbers.parse(number,"RO")
service=carrier.name_for_valid_number(survice_name,"en")
print(service)
