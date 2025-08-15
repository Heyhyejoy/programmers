SELECT COUNT(*) AS users
FROM user_info
WHERE  joined LIKE ('2021%') AND age > 19 AND age < 30