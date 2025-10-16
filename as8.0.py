def list1(student_username,username):
    output=[]
    for student_username in student_usernames:
      email_address = student_username + "@" + username + ".edu.np"
      output.append(email_address)
    return output


student_usernames = ["ksmith", "rsouza", "lgarber", "aghods", "shassan", "proy"]
username = "thebritishcollege"

output = list1(student_usernames,username)
print(output)
