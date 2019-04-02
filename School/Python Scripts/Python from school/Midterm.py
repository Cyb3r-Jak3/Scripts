print ("Welcome to our log in page. Please enter your username: ")
user = raw_input()
if user == 'VEN002':
    print "Welcome to the Vendor section. Please enter the vendor password: "
    password = raw_input()
    if password == 'vendor':
        print "Login correct. Welcome to the system Vendor"
    else:
        print "Password incorrect"
if user == 'EMP001':
    print "Welcome to the Employee section. Please enter the employee password: "
    password = raw_input()
    if password == 'vendor':
        print "Login correct. Welcome to the system Vendor"
    else:
        print "Password incorrect"
if user == 'CUST111':
    print "Welcome to the Customer section. Please enter the customer password: "
    password = raw_input()
    if password == 'vendor':
        print "Login correct. Welcome to the system Vendor"
    else:
        print "Password incorrect"
else:
    print "Sorry. User", user, "is not recongized. Please try agian."

