## 1. How to Create a New MySQL User

To create a new user in MySQL, use the CREATE USER statement:

```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```

- 'new_user'@'localhost' → Username and host (localhost allows only local connections).
- 'password' → The password for the user.

*To allow access from any host, use:*

```sql
CREATE USER 'new_user'@'%' IDENTIFIED BY 'password';
```

## 2. How to Manage Privileges for a User to a Database or Table
👽
After creating a user, grant them permissions to a specific database or table.

*Grant all privileges on a database*
```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'new_user'@'localhost';
Grant specific privileges
```

*Allow only SELECT and INSERT on a table*

```sql
GRANT SELECT, INSERT ON database_name.table_name TO 'new_user'@'localhost';
```

*Apply changes*

```sql
FLUSH PRIVILEGES;
```

*Revoke privileges*

To remove a privilege:

```sql
REVOKE INSERT ON database_name.table_name FROM 'new_user'@'localhost';
```

## 3. What’s a PRIMARY KEY?

A PRIMARY KEY is a column (or a combination of columns) that uniquely identifies each row in a table.

<ins>**Example**</ins>:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,  -- Unique identifier
    name VARCHAR(100)
);
```

- Ensures uniqueness.
- Prevents NULL values.

## 4. What’s a FOREIGN KEY?

A FOREIGN KEY is a column that establishes a relationship between two tables.

<ins>**Example**</ins>:

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)  -- Links to users table
);
```

- Ensures referential integrity.
- Prevents orphaned records (e.g., an order must belong to an existing user).

## 5. How to Use NOT NULL and UNIQUE Constraints

- **NOT NULL** → Ensures a column cannot be NULL.
- **UNIQUE** → Ensures all values in a column are distinct.

<ins>**Example**</ins>:

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE, -- No duplicate emails
    name VARCHAR(100) NOT NULL -- Must have a name
);
```

## 6. How to Retrieve Data from Multiple Tables in One Request

Using JOINs (covered below) or subqueries.

<ins>**Example using JOIN**</ins>:

```sql
SELECT users.name, orders.id
FROM users
JOIN orders ON users.id = orders.user_id;
```

## 7. What Are Subqueries?

A subquery is a query inside another query.

<ins>**Example**</ins>: Get users who placed an order:

```sql
SELECT name FROM users WHERE id IN (SELECT user_id FROM orders);
```

- The inner query runs first.
- The outer query retrieves users whose id exists in the result of the inner query.

## 8. What Are JOIN and UNION?

- **JOIN** → Combines rows from multiple tables based on a related column.
- **UNION** → Combines results from multiple queries into one result set.

<ins>**Example of UNION**</ins>:

```sql
SELECT name FROM users
UNION
SELECT name FROM employees;
```
Both queries must return the same number of columns and matching data types.

## 9. What Does DCL Mean?

DCL (**Data Control Language**) deals with database access control:

- **GRANT** → Assigns permissions.
- **REVOKE** → Removes permissions.

<ins>**Example**</ins>:

```sql
GRANT SELECT, INSERT ON database_name.* TO 'new_user'@'localhost';
REVOKE INSERT ON database_name.* FROM 'new_user'@'localhost';
```
## 10. Which JOIN Types Exist?

INNER JOIN (Default) → Returns only matching records.

```sql
SELECT users.name, orders.id
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

LEFT JOIN → Returns all records from the left table + matching records from the right.

```sql
SELECT users.name, orders.id
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

RIGHT JOIN → Returns all records from the right table + matching records from the left.

```sql
SELECT users.name, orders.id
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;
```

FULL JOIN (Not available in MySQL, use UNION instead) → Returns all records from both tables.

```sql
SELECT users.name, orders.id FROM users
LEFT JOIN orders ON users.id = orders.user_id
UNION
SELECT users.name, orders.id FROM users
RIGHT JOIN orders ON users.id = orders.user_id;
```
🚀