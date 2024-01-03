CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    book_name VARCHAR(250) NOT NULL,
    book_author VARCHAR(250) NOT NULL
);

ALTER TABLE books
RENAME TO lib_books;

ALTER TABLE lib_books
ADD book_year INTEGER NULL;

-- ALTER TABLE lib_books
-- DROP COLUMN year;

-- TABLE lib_books ;

INSERT INTO lib_books (book_name, book_author, book_year)
VALUES ('Book1', 'Author1', 1900);
INSERT INTO lib_books (book_name, book_author, book_year)
VALUES ('Book2', 'Author2', 1800);
INSERT INTO lib_books (book_name, book_author, book_year)
VALUES ('Book3', 'Author3', 1700);

UPDATE lib_books
SET book_year = 2000
WHERE book_id = 2;

DELETE FROM lib_books
WHERE book_year = 1700;