-- Make a lsit of best band fans
-- 2. Select the origin and the sum of fans from the metal_bands table.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
