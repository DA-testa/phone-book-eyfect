# Vasīlijs Dvils-Dmirijevs 221RDB381

import random

class PhoneBook:
    def __init__(self, record_count=1000):
        self.prime = random.randint(0, 10000019)
        self.multiplier = random.randint(0, 263)
        self.record_count = record_count
        self.records = [[] for _ in range(record_count)]

    def hash_function(self, text):
        hash_value = 0
        for i in reversed(text):
            hash_value = (hash_value * self.multiplier + ord(i)) % self.prime
        return hash_value % self.record_count

    def add_record(self, number, name):
        hashed_num = self.hash_function(str(number))
        record = self.records[hashed_num]
        for i in range(len(record)):
            if record[i][0] == number:
                record[i] = (number, name)
                return
        record.append((number, name))

    def delete_record(self, number):
        hashed_num = self.hash_function(str(number))
        record = self.records[hashed_num]
        for i in range(len(record)):
            if record[i][0] == number:
                del record[i]
                return

    def find_name(self, number):
        hashed_num = self.hash_function(str(number))
        record = self.records[hashed_num]
        for i in range(len(record)):
            if record[i][0] == number:
                return record[i][1]
        return "not found"


if __name__ == '__main__':
    phone_book = PhoneBook()
    n = int(input())
    answer = []
    for i in range(n):
        query = input().split()
        if query[0] == "add":
            phone_book.add_record(int(query[1]), query[2])
        elif query[0] == "del":
            phone_book.delete_record(int(query[1]))
        elif query[0] == "find":
            answer.append(phone_book.find_name(int(query[1])))
    for name in answer:
        print(name)
