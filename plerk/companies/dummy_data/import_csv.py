import csv
import os
workpath = os.path.dirname(os.path.abspath(__file__))

db_file = os.path.join(workpath, 'test_database.csv')

from plerk.companies.models import Company
from plerk.transactions.models import Transaction

def get_companies():
    with open(db_file, newline='') as f:
        Company.objects.all().delete()
        reader = csv.reader(f)
        data = list(reader)[1:]
        companies = set()
        for row in data:
            if row[0] != '':
                companies.add(row[0].lower())
        for company in companies:
            Company.objects.create(
                name=company,
                status=1
            )
        print("Companies added:")
        print(Company.objects.count())

from plerk.transactions.choices import STATUS_CHOICES_GET

def get_transactions():
    with open(db_file, newline='') as f:
        Transaction.objects.all().delete()
        reader = csv.reader(f)
        data = list(reader)[1:]
        for transaction in data:
            if transaction[0] == '':
                company = None
            else:
                company = Company.objects.get(name=transaction[0].lower())
            Transaction.objects.create(
                company=company,
                price=transaction[1],
                timestamp=transaction[2],
                status_transaction=STATUS_CHOICES_GET[transaction[3]],
                status_approved=True if transaction[4]=='true' else False
            )
        print("Transactions added:")
        print(Transaction.objects.count())