-- 5. List the number of fans for each origin.
-- Order the result by the number of fans in descending order.
SELECT origin AS origin ,SUM(fans) AS nb_Fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_Fans DESC;
