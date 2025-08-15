SELECT COUNT(fish_info.id) AS fish_count 
FROM fish_info
JOIN fish_name_info
    ON fish_info.fish_type = fish_name_info.fish_type
WHERE fish_name_info.fish_name IN ('bass', 'snapper')