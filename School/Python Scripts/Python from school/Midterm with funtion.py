print ("Welcome to our log in page. Please enter your username: ")
user = raw_input()
log_yes = 0
def Login(username, password):
    global log_yes
    print "Welcome to the", username, "section. Please enter the", username, "password"
    looking = raw_input()
    print looking
    if looking == password:
        print "Login Correct. Welcome to the system", username + "."
        log_yes = 1
    else:
        print "Passcode incorrect"
        log_yes = 2
if user == 'EMP001':
    Login('Employee', 'EMP222')
    if log_yes == 1:
        print "Welcome to the system Employee"
elif user == 'VEN002':
    Login('Vendor', 'vendor')
    if log_yes == 1:
        print "Welcome to the system Vendor"
elif user == 'CUST111':
    Login('Customer', 'buynow999')
    if log_yes == 1:
        print "Welcome to the system Customer"
else:
    print "Sorry", user, "is not recongized. Try again."
