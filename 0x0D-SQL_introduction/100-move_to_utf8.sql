-- converts hbtn_0c_o database to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
-- converts database to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts table to utf8
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;
-- converts a field in a table to utf8
ALTER TABLE hbtn_0c_0.first_table MODIFY TO 'name' VARCHAR(256)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
