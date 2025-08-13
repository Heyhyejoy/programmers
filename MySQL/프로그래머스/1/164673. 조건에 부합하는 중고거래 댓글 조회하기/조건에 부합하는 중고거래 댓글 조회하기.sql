-- 코드를 입력하세요
SELECT 
    USED_GOODS_BOARD.title, 
    USED_GOODS_REPLY.board_id, 
    USED_GOODS_REPLY.reply_id, 
    USED_GOODS_REPLY.writer_id, 
    USED_GOODS_REPLY.contents, 
    date_format(USED_GOODS_REPLY.created_date, '%Y-%m-%d') 
    AS created_date
FROM USED_GOODS_BOARD AS USED_GOODS_BOARD
INNER JOIN USED_GOODS_REPLY AS USED_GOODS_REPLY
    ON USED_GOODS_BOARD.board_id = USED_GOODS_REPLY.board_id
WHERE USED_GOODS_BOARD.created_date LIKE '2022-10-%'
ORDER BY USED_GOODS_REPLY.created_date, title