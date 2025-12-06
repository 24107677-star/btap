import csv

def check_login(user,pw);
    with open("users.csv", "r", encoding="utf-8") as f:
        for u, p, r in csv.reader(f):
            if u == user and p == pw:
                return r
    return None
def register_user(user, pw, role="customer"):
    with open("users.csv", "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow([user, pw, role])