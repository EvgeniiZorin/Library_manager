import pandas as pd
import time

df = pd.read_csv('Library.tsv', sep='\t')


def pause():
	time.sleep(2)
	# print('\n')

def main_menu():
	df = pd.read_csv('Library.tsv', sep='\t')
	print(' '*7 + '/' + '='*53 + '\\')
	print('       | Welcome to the Digital Library! How can I help you? |')
	print(' '*7 + '\\' + '='*53 + '/')
	print('---------------------------------------------------------------------')
	print('|              VIEW               |              EDIT               |')
	print('---------------------------------------------------------------------')
	print('| 1) Print all books              | a) Add a new book               |')
	print('| 2) Print all authors            |                                 |')
	print('| 3) Print all books by an author |                                 |')
	print('| 0) Exit                         |                                 |')
	print('---------------------------------------------------------------------')
	choice = input('Your choice: ')
	if choice == '1':
		print(df)
		pause()
		main_menu()
	elif choice == '2':
		authors = df['Author name'].unique()
		for i, j in enumerate(authors, 1):
			print(f"{i}) {j}")
		pause()
		main_menu()
	elif choice == '3':
		author = input('Please write full name of the author, e.g. "Neil Gaiman": ')
		df1 = df[df['Author name'] == author]
		print(df1)
		pause()
		main_menu()
	elif choice == '0':
		print('Goodbye!')
	#####
	elif choice == 'a':
		author_book = input('Please write full name of the author, his work, and language of the book , e.g. "Neil Gaiman - Coraline - ENG": ')
		author_book_list = [i.strip() for i in author_book.split('-')]
		# author = author_book_list[0]; book = author_book_list[1]; language = author_book_list[2]
		# print(f"Your author: {author_book_list[0]}; your book: {author_book_list[1]}; your language: {author_book_list[2]}")
		df1 = df[ (df['Author name'] == author_book_list[0]) & (df['Book'] == author_book_list[1]) ]
		# Book doesn't exist in the library
		if len(df1) == 0:
			print('This book doesn\'t exist in the library! ')
			df3 = df.append({'Author name': author_book_list[0], 'Book': author_book_list[1], 'Language available': author_book_list[2]}, ignore_index=True)
			df3.to_csv('Library.tsv', sep='\t', index=False)
			print('Added successfully!')
			print(df3[ (df3['Author name'] == author_book_list[0]) & (df3['Book'] == author_book_list[1]) ])
		# Book exists
		if len(df1) > 0:
			langs = list(df1['Language available'])[0].split(',')
			# Language already exists
			if author_book_list[2] in langs:
				print('Sorry, book in this language already exists:')
				print(df1)
			# This language isn't there yet
			else:
				print('The book exists, but in other languages - let\'s add it...')
				for index, row in df.iterrows():
					if df['Author name'][index] == author_book_list[0] and df['Book'][index] == author_book_list[1]:
						df['Language available'][index] = df['Language available'][index] + ',' + author_book_list[2]
						print('Added successfully!')
						print(df[ (df['Author name'] == author_book_list[0]) & (df['Book'] == author_book_list[1]) ])
						df.to_csv('Library.tsv', sep='\t', index=False)
						break
		pause()
		main_menu()


main_menu()