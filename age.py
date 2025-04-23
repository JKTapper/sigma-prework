import datetime

def age(birth_date_string):
    birth_date_values = birth_date_string.split('-')
    day = int(birth_date_values[0])
    month = int(birth_date_values[1])
    year = int(birth_date_values[2])
    birth_date = datetime.datetime(year,month,day)
    age = datetime.datetime.now() - birth_date
    years = age.days // 365
    return years

if __name__ == '__main__':
    user_date_input = input("what date were you born on?")
    age_in_years = age(user_date_input)
    print(age_in_years)