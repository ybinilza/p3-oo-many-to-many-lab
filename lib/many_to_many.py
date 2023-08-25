class Author:

    all = []

    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self,book, date, royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        total_royalties = 0
        author_contracts = self.contracts()
        for contracts in author_contracts:
            total_royalties += contracts.royalties

        return total_royalties

class Book:
    all = []

    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self,author,book,date,royalties):
        self.add_author(author)
        self.add_book(book)
        self.validate_date(date)
        self.validate_royalties(royalties)
        Contract.all.append(self)

    def add_author(self, author):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception()
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception()
        
    def validate_date(self, date):
        if(type(date) == str):
            self.date = date
        else:
            raise Exception()
    
    def validate_royalties(self, royalties):
        if(type(royalties) == int):
            self.royalties = royalties
        else:
            raise Exception()

    @classmethod 
    def contracts_by_date(cls):
        contracts_date = sorted(cls.all, key=lambda x:x.date)

        return contracts_date
    
