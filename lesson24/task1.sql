SELECT _employees.first_name, _employees.last_name, _employees.department_id, _department.department_name
FROM _employees
JOIN _department ON _employees.department_id = _department.department_id ;

SELECT _employees.first_name, _employees.last_name, _department.department_name, _locations.city, _locations.state_province
FROM _employees
JOIN _department ON _employees.department_id = _department.department_id
JOIN _locations ON _department.location_id = _locations.location_id ;

SELECT _employees.first_name, _employees.last_name, _employees.department_id, _department.department_name
FROM _employees
JOIN _department ON _employees.department_id = _department.department_id
WHERE _employees.department_id = 40 OR _employees.department_id = 80 ;

SELECT _employees.first_name, _employees.last_name, _department.department_id, _department.department_name
FROM _employees
RIGHT JOIN _department ON _employees.department_id = _department.department_id ;

SELECT a.first_name AS "employee name", b.first_name AS "manager name"
FROM _employees a
JOIN _employees  b ON a.manager_id = b.employee_id ;

SELECT _jobs.job_title, CONCAT(_employees.first_name, ' ', _employees.last_name) AS "full_name", (CAST(_jobs.max_salary AS INTEGER) - _employees.salary) AS "diff_salary"
FROM _jobs
JOIN _employees ON _jobs.job_id = _employees.job_id ;

SELECT _jobs.job_title, ROUND(AVG(_employees.salary), 2)
FROM _jobs
JOIN _employees ON _jobs.job_id = _employees.job_id
GROUP BY _jobs.job_title ;

SELECT CONCAT(_employees.first_name, ' ', _employees.last_name) AS "full_name", _employees.salary
FROM _employees
JOIN _department ON _employees.department_id = _department.department_id
JOIN _locations ON _department.location_id = _locations.location_id
WHERE _locations.city = 'London';

SELECT _department.department_name, COUNT(_employees.department_id) AS "employees_num"
FROM _department
JOIN _employees ON _department.department_id = _employees.department_id
GROUP BY _department.department_name ;