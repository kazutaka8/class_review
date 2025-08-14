class Customer:
    # 各問のコードが期待通り動作するように実装

    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            fee = 0
        elif self.age < 20:
            fee = 1000
        elif self.age >= 75:
            fee = 500
        elif self.age >= 65:
            fee = 1200
        else:
            fee = 1500
        return fee

    def info_csv(self):
        info = f"{self.full_name()},{self.age},{self.entry_fee()}"
        return info

    # 指定した区切り文字で出力
    def info_delimited(self, delimiter):
        info = f"{self.full_name()}{delimiter}{self.age}{delimiter}{self.entry_fee()}"
        return info


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力

print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力

print(ken.info_delimited(","))
print(tom.info_delimited(","))
print(ieyasu.info_delimited(","))

print(ken.info_delimited("\t"))
print(tom.info_delimited("\t"))
print(ieyasu.info_delimited("\t"))

print(ken.info_delimited("|"))
print(tom.info_delimited("|"))
print(ieyasu.info_delimited("|"))
