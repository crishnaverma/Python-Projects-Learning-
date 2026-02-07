class Book:
    cout = 0
    def __init__(self,tittle,author):
        self.tittle = tittle
        self.author = author
        self.list_of_review = []
    

    def add_review(self,review):
        self.list_of_review.append(review)


    def count(self):
        print(f"Total Reviews {len(self.list_of_review)}")


    def display_review(self):
        if not self.list_of_review:
            print("no reviews")
        else:
            print ("reviews")
            for review in self.list_of_review:
                print("-",review)


b1 = Book("Atomic Habits", "James Clear")

b1.add_review("Very motivating")
b1.add_review("Easy to understand")
b1.count()
b1.display_review()
