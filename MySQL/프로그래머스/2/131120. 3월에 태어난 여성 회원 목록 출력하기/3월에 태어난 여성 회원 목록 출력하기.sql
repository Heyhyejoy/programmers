-- 코드를 입력하세요
SELECT member_id, member_name, gender, 
date_format(date_of_birth, '%Y-%m-%d') AS date_of_birth 
FROM member_profile
WHERE date_of_birth LIKE '%-03-%' AND tlno != 'NULL' AND gender = 'W'
ORDER BY member_id