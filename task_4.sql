-- Query to get full description of the books table
SELECT
    TABLE_NAME,
    COLUMN_NAME,
    COLUMN TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    IS_NULLABLE,
    COLUMN_DEFAULT

FROM
    INFORMATION_SCHEMA.COLUMNS

WHERE
    TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'Books';