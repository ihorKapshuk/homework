SELECT first_name AS "First name", last_name AS "Last name" FROM _employees;

SELECT * FROM _employees
WHERE department_id = 10;

SELECT * FROM _employees
ORDER BY first_name DESC;

SELECT first_name, last_name, salary, 0.12 * salary AS "PF" FROM _employees;

SELECT * FROM _employees
WHERE salary = (
    SELECT MAX (salary)
    FROM _employees
);

SELECT * FROM _employees
WHERE salary = (
    SELECT MIN (salary)
    FROM _employees
);

SELECT CONCAT(first_name, ' ', last_name) AS "Full name",
ROUND(salary / 12.0, 2) AS "salary per month"
FROM _employees ;