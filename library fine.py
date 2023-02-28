days=int(input("Enter the no.of days:"))
if days-15==0 :
    fine=0
    print("ON due day: No fine ",fine)
elif days-15<=5:
    fine=(days-15)*0.70
    print("the fine amount:",float(fine))
elif days-15>=5 and days-15<=10:
    fine=(days-15)*1.80
    print("The fine amount :",float(fine))
elif days-15<10:
    fine=0
    print("The fine is zero")
else :
    fine=(days-15)*100
    print("The fine amount :",int(fine))
print("hello world!")
    

