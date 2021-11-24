authors_price = pd.merge(authors, books, on = 'author_id', how = 'outer')

print(authors_price)