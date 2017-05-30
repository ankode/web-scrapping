import mechanize
 
br = mechanize.Browser()
username=""
password=""
# br.set_handle_robots(False)
br.open("http://i-on.in/loginpage.aspx")
br.select_form(nr=0)
br['txtUserName'] = username
br['txtlogPassword'] = password
result = br.submit().read()
print result
