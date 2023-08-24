"""
Write a function called email_validator that takes a list of 
emails and checks if the emails are valid. The function returns a 
list of only valid emails. A valid email address will have the
following - @ symbol (if the @ sign is at the beginning of the 
name, the email is invalid. If there are more than one @signs, 
the email is invalid. All valid emails must have a dot com at the 
end (.com), if not, the email is invalid.
"""


def email_validator(addy: list) -> list:
    new = []
    for e in addy:
        if (
            e.endswith(".com")
            and not e.startswith("@")
            and e.count("@") == 1
            and "@." not in e
        ):
            new.append(e)
    return new


emails = ["ben@mail.com", "john@mail.cm", "kenny@gmail.com", "@list.com"]
print(email_validator(addy=emails))
